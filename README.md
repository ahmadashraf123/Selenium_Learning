# Selenium WebDriver — Interaction Patterns (Python)

A reference collection of **Selenium WebDriver interaction patterns in Python** — one focused script per browser-automation problem.

Each file is self-contained and solves one thing: handling a JavaScript alert, driving a date picker, working across multiple windows, dealing with hidden elements, and so on. It's the set of techniques a UI automation suite is built out of, kept separate so each can be read on its own.

For a full test framework built on these patterns — Page Object Model, PyTest, data-driven tests, reporting — see
**[Automation_Framework_pageObjectModel](https://github.com/ahmadashraf123/Automation_Framework_pageObjectModel)**.

---

## Patterns Covered

**Element interaction**
| Script | Pattern |
|---|---|
| `elementmethod.py` | Core WebElement methods |
| `getattribute.py` | Reading element attributes |
| `stateofelement.py` | Checking enabled / displayed / selected state |
| `hiddenelement.py` | Locating and handling hidden elements |
| `checkbox.py` · `radiobutton.py` | Checkbox and radio group handling |

**Dropdowns & inputs**
| Script | Pattern |
|---|---|
| `singleselectdropdown.py` · `handledropdown2.py` | `<select>` dropdowns via the Select class |
| `handleautosuggestion.py` | Autosuggest / typeahead fields |
| `calenders.py` | Date picker navigation |
| `handleSlider.py` | Slider control via Actions |

**Mouse & keyboard**
| Script | Pattern |
|---|---|
| `MouseHower.py` | Hover with ActionChains |
| `right_click_double_click.py` | Context click and double click |
| `DragandDrop.py` | Drag and drop |

**Browser & window control**
| Script | Pattern |
|---|---|
| `browsercommonds.py` | Navigation, window, and browser commands |
| `demomultiplewindows.py` | Switching between windows and tabs |
| `alerts.py` | JavaScript alerts, confirms and prompts |
| `Loginbrowserauthpopup.py` | Browser-level auth popups |
| `clear_cache.py` | Clearing browser cache |

**Waits, JS & capture**
| Script | Pattern |
|---|---|
| `implicit_wait.py` | Implicit waits |
| `javascripthandling.py` | JavaScript execution via `execute_script` |
| `capturescreenshot.py` | Screenshot capture |

---

## Setup

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

pip install -r requirements.txt
```

Browser drivers are resolved automatically by `webdriver-manager` — no manual downloads.

Run any script directly:

```bash
python alerts.py
```

---

## Author

**Ahmad Khan** — SQA Automation Engineer
[GitHub](https://github.com/ahmadashraf123) · [LinkedIn](https://www.linkedin.com/in/ahmad-khan-SQA/)
