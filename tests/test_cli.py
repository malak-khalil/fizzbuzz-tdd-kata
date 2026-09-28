import sys

from fizzbuzz_tdd_kata.cli import build_parser, main


def test_parser_accepts_single_number():
    args = build_parser().parse_args(["15"])
    assert args.n == 15


def test_parser_accepts_range():
    args = build_parser().parse_args(["--start", "1", "--end", "5"])
    assert args.start == 1
    assert args.end == 5


def test_main_single_number(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["fizzbuzz-kata", "15"])
    main()
    assert capsys.readouterr().out == "FizzBuzz\n"


def test_main_range(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        ["fizzbuzz-kata", "--start", "1", "--end", "5"],
    )
    main()
    assert capsys.readouterr().out == "1\n2\nFizz\n4\nBuzz\n"
