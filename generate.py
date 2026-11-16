# /// script
# requires-python = ">=3.10"
# dependencies = ["rich"]
# ///
"""Render the GitHub profile README as a terminal-style UI.

Usage:  uv run generate.py      (or: pip install rich && python generate.py)
"""

from rich import box
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.table import Table
from rich.text import Text
from rich.tree import Tree

WIDTH = 100
HANDLE = "hustavojhon"
PORTFOLIO = "https://hustavojhon.vercel.app/"
GITHUB = f"https://github.com/{HANDLE}"
INSTAGRAM = f"https://www.instagram.com/{HANDLE}/"

console = Console(record=True, width=WIDTH)

BANNER = r"""
██╗  ██╗██╗   ██╗███████╗████████╗ █████╗ ██╗   ██╗ ██████╗      ██╗██╗  ██╗ ██████╗ ███╗   ██╗
██║  ██║██║   ██║██╔════╝╚══██╔══╝██╔══██╗██║   ██║██╔═══██╗     ██║██║  ██║██╔═══██╗████╗  ██║
███████║██║   ██║███████╗   ██║   ███████║██║   ██║██║   ██║     ██║███████║██║   ██║██╔██╗ ██║
██╔══██║██║   ██║╚════██║   ██║   ██╔══██║╚██╗ ██╔╝██║   ██║██   ██║██╔══██║██║   ██║██║╚██╗██║
██║  ██║╚██████╔╝███████║   ██║   ██║  ██║ ╚████╔╝ ╚██████╔╝╚█████╔╝██║  ██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝  ╚═══╝   ╚═════╝  ╚════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
""".strip("\n")


# ── title bar ──────────────────────────────────────────────────────────────
def title_bar() -> Table:
    bar = Table.grid(expand=True)
    bar.add_column(justify="left")
    bar.add_column(justify="right")
    bar.add_row(
        Text.from_markup(f"[b reverse] {HANDLE}@arch [/] [dim]~/profile/README.md[/]"),
        Text.from_markup(
            "[b reverse] 1 [/] about  [b reverse] 2 [/] stack  "
            "[b reverse] 3 [/] projects  [b reverse] 4 [/] contact"
        ),
    )
    return bar


# ── [1] about ──────────────────────────────────────────────────────────────
ABOUT = f"""\
[b]Gustavo Jhon[/] // Systems Engineering Student
Software Developer from [link=https://www.google.com/maps/place/Cusco]Cusco, Peru[/].

I'm passionate about building software,
exploring new technologies, and creating
tools that solve real-world problems.

I enjoy working close to the system,
experimenting with Rust, Linux, artificial
intelligence and open source.

I believe in learning by building, keeping
things simple, and making software that
matters.

[green]> follow me [b link={INSTAGRAM}]@{HANDLE}[/][/]"""


def about_panel() -> Panel:
    return Panel(
        ABOUT,
        box=box.DOUBLE,
        border_style="blue",
        title="[b][ 1 ] Hi there",
        title_align="left",
        width=50,
        padding=(1, 2),
    )


# ── identity tree ──────────────────────────────────────────────────────────
INTERESTS = {
    "[rs] Rust & Systems Programming": [
        "Building command-line tools and TUIs",
        "Exploring performance and systems design",
        "Creating software with Rust",
    ],
    "[ai] Artificial Intelligence": [
        "AI-powered applications",
        "Data analysis & intelligent systems",
        "Exploring practical AI engineering",
    ],
    "[lx] Linux & Open Source": [
        "Arch Linux / Omarchy",
        "Open-source enthusiast",
        "Developer tools & terminal workflows",
    ],
    "[se] Software Engineering": [
        "Full-stack development",
        "Backend architecture & APIs",
        "Building real-world applications",
    ],
    "[++] Other interests": [
        "UI/UX & Graphic Design",
        "Terminal interfaces & minimalism",
        "Vim & developer productivity",
        "Dota 2 . Music . Technology",
    ],
}


def identity_tree() -> Tree:
    tree = Tree(
        f"[b]>_ [link={PORTFOLIO}]Gustavo Jhon[/][/]", guide_style="bold cyan"
    )
    for branch, leaves in INTERESTS.items():
        node = tree.add(f"[b]{branch.replace('[', chr(92) + '[')}", guide_style="green")
        for leaf in leaves:
            node.add(leaf)
    return tree


# ── sysinfo (neofetch style) ───────────────────────────────────────────────
LOGO = r"""
       /\
      /  \
     /\   \
    /      \
   /   ,,   \
  /   |  |  -\
 /_-''    ''-_\
""".rstrip("\n")

SYSINFO = [
    ("user", f"{HANDLE}@github"),
    ("role", "Systems Engineering Student"),
    ("job", "Software Developer"),
    ("os", "Arch Linux / Omarchy"),
    ("wm", "Hyprland"),
    ("editor", "Vim / Neovim"),
    ("shell", "zsh"),
    ("focus", "Rust . AI . Open Source"),
    ("motto", "learn by building"),
]


def sysinfo_panel() -> Panel:
    info = Table.grid(padding=(0, 1))
    info.add_column(style="b cyan", justify="right")
    info.add_column()
    for key, value in SYSINFO:
        info.add_row(key, value)
    palette = Text.from_markup(
        " ".join(f"[{c}]███[/]" for c in ("red", "green", "yellow", "blue", "magenta", "cyan"))
    )
    info.add_row("", "")
    info.add_row("", palette)

    grid = Table.grid(padding=(0, 2))
    grid.add_row(Text(LOGO, style="bold cyan"), info)
    return Panel(
        grid,
        box=box.ROUNDED,
        border_style="cyan",
        title="[b]sysinfo",
        title_align="left",
        width=WIDTH,
    )


# ── [2] stack ──────────────────────────────────────────────────────────────
STACK = [
    ("languages", "Rust  Python  C#  Java  Dart"),
    ("backend", ".NET  Spring Boot  REST APIs"),
    ("ai / data", "AI-powered apps  Data analysis"),
    ("tooling", "Git  GitHub  Vim  Linux  CLI / TUI"),
    ("practices", "Clean Code  SOLID  OOP  LINQ"),
]


def stack_panel() -> Panel:
    table = Table(box=box.SIMPLE_HEAD, expand=True, header_style="b magenta")
    table.add_column("layer", style="b", no_wrap=True)
    table.add_column("tools")
    for layer, tools in STACK:
        table.add_row(layer, tools)
    return Panel(
        table,
        box=box.ROUNDED,
        border_style="magenta",
        title="[b][ 2 ] stack",
        title_align="left",
        width=WIDTH,
    )


# ── [3] projects ───────────────────────────────────────────────────────────
PROJECTS = [
    ("SENTRI", "TUI", "Opportunity discovery from the terminal"),
    ("BASIC", "TUI", "Learning & productivity in the terminal"),
    ("AkilFlow", "ERP", "Business management system"),
    ("WASIYUQ", "PLATFORM", "Modern software platform"),
]


def projects_panel() -> Panel:
    table = Table(box=box.SIMPLE_HEAD, expand=True, header_style="b yellow")
    table.add_column("#", style="dim", justify="right", width=2)
    table.add_column("project", style="b", no_wrap=True)
    table.add_column("type", style="yellow", no_wrap=True)
    table.add_column("description")
    for i, (name, kind, desc) in enumerate(PROJECTS, start=1):
        table.add_row(f"{i:02}", name, f"[{kind}]".replace("[", "\\["), desc)
    return Panel(
        table,
        box=box.ROUNDED,
        border_style="yellow",
        title="[b][ 3 ] projects",
        title_align="left",
        width=WIDTH,
    )


# ── [4] contact ────────────────────────────────────────────────────────────
def contact_panel() -> Panel:
    links = Table.grid(padding=(0, 3), expand=True)
    for _ in range(3):
        links.add_column(justify="center")
    links.add_row(
        f"[b]web[/]  [link={PORTFOLIO}]hustavojhon.vercel.app[/]",
        f"[b]github[/]  [link={GITHUB}]@{HANDLE}[/]",
        f"[b]instagram[/]  [link={INSTAGRAM}]@{HANDLE}[/]",
    )
    return Panel(
        links,
        box=box.ROUNDED,
        border_style="green",
        title="[b][ 4 ] contact",
        title_align="left",
        width=WIDTH,
    )


# ── status line ────────────────────────────────────────────────────────────
def status_line() -> Table:
    bar = Table.grid(expand=True)
    bar.add_column(justify="left")
    bar.add_column(justify="center")
    bar.add_column(justify="right")
    bar.add_row(
        Text.from_markup("[b reverse] NORMAL [/] README.md"),
        Text.from_markup('[i dim]"I am less of a failure than I was before."[/]'),
        Text.from_markup("utf-8 [b reverse] q [/] quit"),
    )
    return bar


def render() -> None:
    console.print(title_bar())
    console.print(Rule(style="dim"))
    console.print(Align.center(Text(BANNER, style="bold cyan")))
    console.print(
        Align.center(
            Text.from_markup(
                "[dim]systems engineering student  ::  software developer  ::  rust . ai . linux[/]"
            )
        )
    )
    console.print()
    row = Table.grid(padding=(0, 2))
    row.add_row(about_panel(), identity_tree())
    console.print(row)
    console.print()
    console.print(sysinfo_panel())
    console.print(stack_panel())
    console.print(projects_panel())
    console.print(contact_panel())
    console.print(Rule(style="dim"))
    console.print(status_line())


CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

if __name__ == "__main__":
    render()
    console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
