from rich.console import Console
from rich.table import Table
import mmh3
import math
import time
import json

class HyperLogLog:
    def __init__(self, p=5):
        self.p = p
        self.m = 1 << p
        self.registers = [0] * self.m
        self.alpha = self._get_alpha()
        self.small_range_correction = 5 * self.m / 2  # Поріг для малих значень

    def _get_alpha(self):
        if self.p <= 16:
            return 0.673
        elif self.p == 32:
            return 0.697
        else:
            return 0.7213 / (1 + 1.079 / self.m)

    def add(self, item):
        x = mmh3.hash(str(item), signed=False)
        j = x & (self.m - 1)
        w = x >> self.p
        self.registers[j] = max(self.registers[j], self._rho(w))

    def _rho(self, w):
        return len(bin(w)) - 2 if w > 0 else 32

    def count(self):
        Z = sum(2.0 ** -r for r in self.registers)
        E = self.alpha * self.m * self.m / Z
        
        if E <= self.small_range_correction:
            V = self.registers.count(0)
            if V > 0:
                return self.m * math.log(self.m / V)
        
        return E

def loader(container):
    with open("data/lms-stage-access.log", "r") as fh:
        for log_entry in fh:
            try:
                log_data = json.loads(log_entry)
                ip_address = log_data.get("remote_addr")
                if ip_address:
                    container.add(ip_address)
            except json.JSONDecodeError:
                print("Log processing error: invalid JSON")

def count_exact():
    ips = set()
    start = time.time()
    loader(ips)
    return len(ips), time.time() - start


def count_hyper_log_log():
    hyper_log_log = HyperLogLog()
    start = time.time()
    loader(hyper_log_log)
    return hyper_log_log.count(), time.time() - start

def display_comparison(exact_count, hyper_log_log_count, exact_time, hyper_log_log_time):
    console = Console()

    table = Table(title="Comparison Results")

    table.add_column("", justify="left", style="bold")
    table.add_column("Exact Count", justify="center", style="bold")
    table.add_column("HyperLogLog", justify="center", style="bold")

    table.add_row("Unique Elements", f"[dim]{exact_count}[/dim]", f"[dim]{hyper_log_log_count}[/dim]")
    table.add_row("Execution Time (sec.)", f"[dim]{exact_time}[/dim]", f"[dim]{hyper_log_log_time}[/dim]")

    console.print(table)

if __name__ == "__main__":
    exact_count, exact_time = count_exact()
    hyper_log_log_count, hyper_log_log_time = count_hyper_log_log()
    display_comparison(exact_count, hyper_log_log_count, exact_time, hyper_log_log_time)