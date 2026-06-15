# TODO: Expand OOPCodeBase into a Full OOP Demonstration

Current state: the repo demonstrates **encapsulation** (state + behavior
bundled in `Printer`) and **packaging/imports**. The items below add the
remaining OOP pillars — **inheritance**, **polymorphism**, and
**abstraction** — plus a few code-quality items, roughly in the order
they build on each other.

---

## 1. Abstraction — introduce a base class

- [ ] Create an abstract base class `Device` (in `src/devices/device.py`
      or similar) using `abc.ABC` and `@abstractmethod`.
- [ ] Give `Device` a couple of shared abstract methods that any office
      device would need, e.g. `check_status()` and `power_on()`.
- [ ] Add a shared concrete attribute or method too (e.g. `device_name`,
      or a `__repr__`) so subclasses get something "for free" — this is
      what makes inheritance worth demonstrating.
- [ ] Make `Printer` inherit from `Device` and implement the abstract
      methods.
- [ ] In the README, add a short section explaining *why* `Device` is
      abstract — i.e., "you'd never instantiate a bare `Device`."

## 2. Inheritance — add a sibling/subclass of Printer

- [ ] Create `ColorPrinter(Printer)` (or `ScannerPrinter`, `3DPrinter` —
      pick whatever's fun) that:
  - [ ] Adds a new attribute not present in `Printer` (e.g. `toner_levels`
        as a dict of colors, or `scan_resolution`).
  - [ ] Calls `super().__init__(...)` to reuse the base constructor.
  - [ ] Overrides at least one method (see Polymorphism below).
- [ ] Confirm `ColorPrinter` can do everything `Printer` can (the "is-a"
      relationship) — e.g. `printer.print_document()` still works
      unchanged via inheritance.

## 3. Polymorphism — override and demonstrate dynamic dispatch

- [ ] Override `notify_low_ink()` (or rename per item 6) in `ColorPrinter`
      to check *multiple* ink/toner levels instead of one.
- [ ] In `main.py`, build a list containing both a `Printer` and a
      `ColorPrinter`, then loop over it calling the *same* method name on
      each — show that each object responds according to its own class,
      without `main.py` needing to know which is which.
- [ ] Optionally add a second override that calls `super().method()` and
      extends the behavior, to show "extend, don't just replace."

## 4. Encapsulation cleanup (sharpen what's already there)

- [ ] Convert `ink_level` / `paper_level` to "protected" attributes
      (`_ink_level`, `_paper_level`) and expose them via `@property`
      getters.
- [ ] Add validation in a `@<attr>.setter` (e.g. reject negative values,
      or clamp to 0–100) — this is the canonical "why encapsulation
      matters" example: direct attribute access can't enforce invariants,
      a property can.
- [ ] Update internal methods (`print_document`, etc.) to use the
      property names consistently.

## 5. Composition (optional but valuable — "has-a" vs "is-a")

- [ ] Create a small `InkCartridge` or `PaperTray` class with its own
      state/behavior (e.g. `InkCartridge.refill()`, `.is_empty()`).
- [ ] Have `Printer` *hold* an `InkCartridge` instance as an attribute
      instead of a raw `ink_level` number.
- [ ] Update the README's diagrams to show this as a "has-a" relationship,
      contrasted with the "is-a" inheritance relationships above.

## 6. Naming / behavior cleanup (from earlier review)

- [ ] Rename `notify_low_ink` / `notify_out_of_paper` to something that
      matches their actual (always-prints-a-status-line) behavior —
      e.g. `report_ink_status` / `report_paper_status` — or split out a
      genuinely conditional `notify_*` method that *only* prints on
      warning/error.
- [ ] Replace the pseudo-docstring string literal inside
      `if __name__ == "__main__":` in `hello.py` with a regular `#`
      comment, since it isn't actually treated as a docstring there.

## 7. Package structure review

- [ ] Decide whether both `src/__init__.py` *and*
      `src/say_hello/__init__.py` re-exporting `Printer` is intentional
      teaching redundancy or accidental duplication — either document the
      reason in the README or collapse to one layer.
- [ ] As new classes are added (`Device`, `ColorPrinter`, `InkCartridge`),
      decide on a package layout — e.g. `src/devices/` containing
      `device.py`, `printer.py`, `color_printer.py`, `ink_cartridge.py` —
      and update the README's file dependency diagram to match.

## 8. Tests (ties back into DSA/TDD habits)

- [ ] Add a `tests/` directory with `unittest`-based tests for each class.
- [ ] Test the abstract base class *cannot* be instantiated directly
      (`Device()` should raise `TypeError`).
- [ ] Test that `ColorPrinter` correctly overrides `Printer` behavior
      (polymorphism check).
- [ ] Test property setter validation from item 4 (e.g. setting a
      negative ink level raises or clamps as designed).

## 9. README updates

- [ ] Add a section mapping each of the four OOP pillars to a specific
      class/method in the repo, so a reader can match concept → code
      directly.
- [ ] Update the file dependency diagram and execution flow chart to
      reflect the new classes once added.

---

### Suggested order of attack

1. Items 6 (quick naming/comment fixes — low effort, immediate clarity)
2. Item 1 (abstract base class — foundation for everything else)
3. Item 2 + 3 together (subclass + override, since they're naturally paired)
4. Item 4 (properties/encapsulation polish)
5. Item 5 (composition, if time allows)
6. Item 7 (package structure, once new files exist)
7. Item 8 (tests — good to do incrementally as each class is added,
   not all at the end)
8. Item 9 (README, as a final pass tying it all together)
