# Library Catalog And Selection Rules

## Table Of Contents

1. Selection principles
2. Design system options
3. iOS stack options
4. Android stack options
5. React Native stack options
6. Flutter stack options
7. Hybrid stack options
8. Output mapping contract

## Selection Principles

Choose for fit, not popularity:

- Match platform conventions first
- Preserve accessibility capability
- Prefer mature component coverage for delivery speed
- Avoid adding libraries that duplicate existing stack
- Keep theming and tokens maintainable

## Design System Options

Use one of these as baseline:

- Material 3
- Apple Human Interface Guidelines
- Custom branded system
- Hybrid: Material-like behavior with custom visual tokens

## iOS Stack Options

- SwiftUI (native-first default)
- UIKit + modern compositional patterns
- SwiftUI with UIKit bridges

## Android Stack Options

- Jetpack Compose (native-first default)
- Android Views + Material Components XML
- Compose + View interop for gradual migration

## React Native Stack Options

Broad, practical options:

- React Native Paper
- NativeBase
- UI Kitten
- React Native Elements
- Tamagui
- GlueStack UI
- Restyle (Shopify)
- Custom primitives on top of React Native core

Use with ecosystem tools as needed:

- React Navigation
- React Hook Form
- Reanimated / Gesture Handler

## Flutter Stack Options

- Material widgets
- Cupertino widgets
- Hybrid Material + Cupertino
- Flutter Community UI packages by feature need

Use with architecture tooling as needed:

- Bloc / Cubit
- Riverpod
- Provider

## Hybrid Stack Options

- Ionic + Capacitor + Ionic UI components
- KMP + Compose Multiplatform (where org supports it)

## Output Mapping Contract

For each key screen, include:

- Selected design system
- Selected UI library
- Mapping of generic intents to concrete components
- Required props/modifiers
- State behavior mapping (loading, error, disabled, success)
- Accessibility implementation notes
