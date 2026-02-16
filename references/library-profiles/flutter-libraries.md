# Flutter Library Profile

## Core Options

- Material widgets
- Cupertino widgets
- Hybrid Material + Cupertino strategy

## Common Package Layer

- Forms/validation helpers by project preference
- State management: Bloc, Riverpod, Provider
- Motion packages only when default transitions are insufficient

## Design System Alignment

- Material 3 for Android-weighted products
- Cupertino emphasis for iOS-native feel
- Shared token layer for branded cross-platform consistency

## Component Mapping Hints

- Primary action button -> `FilledButton`, `ElevatedButton`
- Text input -> `TextField`, `TextFormField`
- Selection controls -> `Checkbox`, `Switch`, `Radio`
- List row -> `ListTile` or custom row in `ListView`
- Feedback -> `SnackBar`, inline `Banner`, dialog
- Modal/sheet -> `showModalBottomSheet`, `AlertDialog`

## State And Accessibility Notes

- Use explicit state widgets for loading, empty, and error
- Provide semantic labels and hints through Semantics
- Validate large text and screen-reader behavior
- Respect motion reduction and platform conventions
