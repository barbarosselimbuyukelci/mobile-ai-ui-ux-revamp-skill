# Mobile Interaction Patterns

## Navigation

Tab bar:

- Use for 3 to 5 top-level destinations.
- Keep labels explicit and short.

Stack navigation:

- Use for deep task flows.
- Keep back behavior predictable.

Bottom sheet:

- Use for contextual actions and low-friction edits.
- Avoid deeply nested sheets.

## Forms

- Prefer short forms with progressive disclosure.
- Validate early but avoid noisy interruptions.
- Keep field labels persistent and unambiguous.
- Preserve input on interruption or app backgrounding.

## States

Define all critical states:

- Loading
- Empty
- Error
- Partial
- Success
- Offline

Each state must include a next action.

## AI Interaction Pattern

For generated outputs:

- Show summary of what was produced.
- Allow inspect details.
- Allow edit or regenerate.
- Show source/context footprint when available.

## Voice + Touch Pattern

Use voice as a complement, not replacement:

- Voice for quick intent capture or hands-busy moments.
- Touch for precision, review, and correction.
- Keep a visible transcript and editable command state.

## Micro-Interaction Pattern

Micro-interactions must communicate:

- Action acknowledged
- Progress and waiting
- Success confirmed
- Error surfaced with recovery

Use motion intentionally and respect reduced-motion preferences.
