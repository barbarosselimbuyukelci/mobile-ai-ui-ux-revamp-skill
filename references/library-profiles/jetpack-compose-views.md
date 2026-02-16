# Android Library Profile

## Primary Stacks

- Jetpack Compose
- Android Views + Material Components
- Compose + Views interop

## Design System Alignment

- Material 3 as default baseline
- Custom token layer allowed on top of Material behaviors

## Component Mapping Hints

- Primary action button -> `Button`, `FilledTonalButton`
- Text input -> `TextField`, `OutlinedTextField`
- Selection control -> `Checkbox`, `Switch`, `RadioButton`
- Tabs -> `TabRow` / `TabLayout`
- List row -> `LazyColumn` item / RecyclerView row
- Modal -> `ModalBottomSheet`, `AlertDialog`

## State And Accessibility Notes

- Use explicit loading and error composables
- Preserve readable semantics for TalkBack
- Keep focus and traversal order predictable
- Respect system font scaling and reduced animation preferences
