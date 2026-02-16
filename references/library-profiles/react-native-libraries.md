# React Native Library Profile

## Common UI Libraries

- React Native Paper
- NativeBase
- UI Kitten
- React Native Elements
- Tamagui
- GlueStack UI
- Restyle-based custom systems

## Supporting Stack

- Navigation: React Navigation
- Forms: React Hook Form
- Motion/Gesture: Reanimated, Gesture Handler

## Design System Alignment

- Material 3 style: React Native Paper is common
- Cross-brand custom systems: Tamagui, Restyle, custom primitives

## Component Mapping Hints

- Primary action button -> library `Button`
- Text input -> library `TextInput` or `Input`
- Selection controls -> `Checkbox`, `Switch`, `Radio`
- List row -> `FlatList` item + library containers
- Feedback -> `Snackbar`, `Toast`, inline `Alert`
- Modal/sheet -> `Modal`, library bottom-sheet component

## State And Accessibility Notes

- Centralize loading/error/empty components for consistency
- Ensure accessibility labels and roles are explicit
- Verify focus and screen-reader flow on both iOS and Android
- Keep touch targets and gesture conflicts under control
