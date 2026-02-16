# iOS Library Profile

## Primary Stacks

- SwiftUI
- UIKit
- SwiftUI + UIKit interop

## Design System Alignment

- Apple HIG for native behavior
- Material-style patterns only when product constraints require it

## Component Mapping Hints

- Primary action button -> `Button` (SwiftUI) / `UIButton` (UIKit)
- Form text input -> `TextField`, `SecureField` / `UITextField`
- Toggle input -> `Toggle` / `UISwitch`
- Segmented control -> `Picker(.segmented)` / `UISegmentedControl`
- List row -> `List` row / `UITableViewCell` or `UICollectionViewCell`
- Modal -> `sheet` / `present(_:animated:)`

## State And Accessibility Notes

- Represent loading with visible progress and disabled conflicting actions
- Provide clear labels, hints, and traits for VoiceOver
- Keep dynamic type and content size adaptability
- Respect reduced motion settings
