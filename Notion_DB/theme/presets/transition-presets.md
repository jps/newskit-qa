Transition presets | NewsKit design system

Presets

Transition presets
==================

A collection of motion attributes combined into a preset to define reusable motion transition from one state to another.

Overview
--------

Transition presets define attributes such as the visual style, size or position of an element across multiple states over time. You can reuse transition presets on multiple elements throughout the system.

* * *

Transition preset properties
----------------------------

Transition presets use a combination of properties:

Token name

Accepted Values

Example

Description

* * *

Predefined transition presets
-----------------------------

Here’s a collection of out-of-the-box transition presets you can apply to elements:

Example

Token

Description

Implementation

You can add your own transition presets. See the [creating a theme](/theme/theming/creating-a-theme/) guide for more details.

* * *

Transition preset states
------------------------

States define the [CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions), duration, delay and transition timing, as well as the initial and final styling of an element.

There are two ways to define transitions:

### 1\. States for transitions triggered upon user interaction

You can apply these transition presets to elements upon user interaction (e.g. changing the background colour of a [button](/components/button/) on hover). The following states are used:

Example

Name

Type

Description

### 2\. States for transitions triggered upon entry and exit of a component

You can apply these transition presets upon entry (mount) and exit (unmount) of a component (e.g. a [modal](/components/modal/) appearing and disappearing). The following states are used and represent class names applied to an element:

Example

Name

Type

Description

* * *

Apply transition presets
------------------------

See the [component defaults page](/theme/theming/component-defaults/) for the different ways to override and apply transition presets to NewsKit components.  
  
For more advanced use cases, access these values from the theme by calling [getTransitionPreset](/theme/theming/using-a-theme/) (a function used to retrieve values from the component defaults or overrides objects) or [getTransitionPresetFromTheme](/theme/theming/using-a-theme/) (used to retrieve token values from theme or component props).

### Trigger transition presets upon user interaction

1\. Here’s the `backgroundColorChange` transition preset.

    1transitionPresets.backgroundColorChange = {
    2  base: {
    3    transitionProperty: 'background-color',
    4    transitionDuration: '{{motions.motionDuration050}}',
    5    transitionTimingFunction: '{{motions.motionTimingEaseOut}}',
    6  },
    7};

2\. When combined with the following `stylePreset`, the background colour transitions between states.

    1stylePresets.box = {
    2  base: {
    3      backgroundColor: '{{colors.purple030}}',
    4    },
    5    hover: {
    6      backgroundColor: '{{colors.purple070}}',
    7    }
    8};

3\. `backgroundColorChange` applied to a simple box element.

    1const Box = styled.div`
    2${getStylePresetFromTheme('box')}
    3${getTransitionPresetFromTheme('backgroundColorChange')}
    4  width: 100px;
    5  height: 100px;
    6`;

### Apply combined transition presets to background and border colours

1\. Here are two transition presets: `backgroundColorChange` and `borderColorChange`.

    1transitionPresets.backgroundColorChange = {
    2  base: {
    3    transitionProperty: 'background-color',
    4    transitionDuration: '{{motions.motionDuration030}}',
    5    transitionTimingFunction: '{{motions.motionTimingEaseOut}}',
    6  },
    7};
    8
    9transitionPresets.borderColorChange = {
    10  base: {
    11    transitionProperty: 'border-color',
    12    transitionDuration: '{{motions.motionDuration050}}',
    13    transitionTimingFunction: '{{motions.motionTimingEaseOut}}',
    14  },
    15};

2\. When combined with the following `stylePreset`, the background and border colours transition between states with different durations.

    1stylePresets.box = {
    2  base: {
    3    backgroundColor: '{{colors.purple030}}',
    4    borderWidth: '{{borders.borderWidth030}}',
    5    borderStyle: 'solid',
    6    borderColor: '{{colors.green020}}',
    7  },
    8  hover: {
    9    backgroundColor: '{{colors.purple070}}',
    10    borderColor: '{{colors.green040}}',
    11  }
    12};

3\. `backgroundColorChange` and `borderColorChange` applied to a simple box component.

    1const Box = styled.div`
    2${getStylePresetFromTheme('box')}
    3${getTransitionPresetFromTheme(['backgroundColorChange', 'borderColorChange'])}
    4  width: 100px;
    5  height: 100px;
    6`;

Apply to all instances

These examples only apply to a single instance of a component. To apply to all instances, use [component defaults](/theme/theming/component-defaults/).

### Trigger transition presets upon mount/unmount

1\. Here’s the `slideLeft` transition preset, used to slide an element in from the left edge of the screen.

    1transitionPresets.slideLeft = {
    2  base: {
    3    transform: 'translateX(-100%)',
    4  },
    5  enter: {
    6    transform: 'translateX(-100%)',
    7  },
    8  enterActive: {
    9    transform: 'translateX(0)',
    10    transitionProperty: 'transform',
    11    transitionDuration: '{{motions.motionDuration020}}',
    12    transitionTimingFunction: '{{motions.motionTimingEaseIn}}',
    13  },
    14  enterDone: {
    15    transform: 'translateX(0)',
    16  },
    17  exit: {
    18    transform: 'translateX(0)',
    19  },
    20  exitActive: {
    21    transform: 'translateX(-100%)',
    22    transitionProperty: 'transform',
    23    transitionDuration: '{{motions.motionDuration020}}',
    24    transitionTimingFunction: '{{motions.motionTimingEaseOut}}',
    25  },
    26  exitDone: {
    27    transform: 'translateX(-100%)',
    28  },
    29};

2\. Apply the transition preset to the drawer in the defaults.

    1export const Drawer = styled.div`
    2  ${getTransitionPreset(
    3    `drawer.panel.left`,
    4    'panel',
    5    'nk-drawer',
    6    )};
    7`;
    8
    9 <Drawer
    10  open
    11  onDismiss={close}
    12  header="Drawer"
    13>
    14  <div>Content</div>
    15</Drawer>

* * *

Extend or override transition presets
-------------------------------------

You can override or combine transition presets to achieve different combinations.

### Code example

Here’s how to override a transition preset applied in the defaults of the [drawer](/components/drawer/) component:

    1 <Drawer
    2  open
    3  onDismiss={close}
    4  header="This is a drawer header"
    5  overrides={{
    6    panel: {
    7      transitionPreset: 'slideRight',
    8    },
    9  }}
    10>
    11  <DrawerContent />
    12</Drawer>

Here’s how to extend two predefined transition presets - `fade` and `moveUp` applied to a modal component. The duration and timing functions of both presets are overridden and delay is added to the `fade` transition preset when the component appears on the screen.  
  
For both transition presets, the duration and timing functions are updated from the enter to the exit state of the transition:

    1<Modal
    2  open={true}
    3  onDismiss={close}
    4  header="This is a modal header."
    5  overrides={{
    6    panel: {
    7      transitionPreset: [
    8        {
    9          extend: 'fade',
    10          enterActive: {
    11            transitionDuration: '{{motions.motionDuration010}}',
    12            transitionTimingFunction: '{{motions.motionTimingEaseOut}}',
    13            transitionDelay: '{{motions.motionDuration010}}',
    14          },
    15          exitActive: {
    16            transitionDuration: '{{motions.motionDuration010}}',
    17            transitionTimingFunction: '{{motions.motionTimingLinear}}',
    18          },
    19        },
    20        {
    21          extend: 'moveUp',
    22          enterActive: {
    23            transitionDuration: '{{motions.motionDuration010}}',
    24            transitionTimingFunction: '{{motions.motionTimingEaseOut}}',
    25            transitionDelay: '{{motions.motionDuration010}}',
    26          },
    27          exitActive: {
    28            transitionDuration: '{{motions.motionDuration010}}',
    29            transitionTimingFunction: '{{motions.motionTimingEaseIn}}',
    30          },
    31        },
    32      ],
    33    },
    34  }}
    35>
    36  {modalContent}
    37</Modal>

* * *

Add custom transition presets to the theme
------------------------------------------

See the [creating a theme](/theme/theming/creating-a-theme/) guide for more details.

* * *

Communicate transition presets in Figma
---------------------------------------

The difficulty in communicating motion in static layouts is a long-standing problem in the design world. It’s often left to developers to figure something out.

To alleviate this problem with page-level transitions, designers should refer to the documentation provided in Figma.

For help communicating designs to engineers, see the [handoff guidance.](https://www.figma.com/proto/kXCrh9MHKAJ878KE2dQOz8/Handoff-Guides---for-engineers-%26-designers?page-id=1%3A544&node-id=275%3A21221&viewport=350%2C48%2C0.13&scaling=min-zoom&starting-point-node-id=275%3A21221&show-proto-sidebar=1&hide-ui=1)

* * *

Accessibility
-------------

Users who experience [motion sensitivity](https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions.html) have the option of a more basic experience that reduces motion where possible.

### Reduce motion for motion sensitivities

The [prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) CSS media feature detects if the user has requested that their operating system or browser minimises the amount of non-essential motion displayed.  
  
We also recommend using the `prefers-reduced-motion` feature on elements with motion. By default, we support this feature for components that have motion applied (e.g. [drawer](/components/drawer/), and [modal](/components/modal/)).  
  
[Check which browsers support reduced motion](https://caniuse.com/prefers-reduced-motion).

### Code example

Here’s how to implement this feature using CSS:

    1@media (prefers-reduced-motion: reduce) {
    2    /* reduced behaviour */
    3}

* * *

Typography Presets
==================

A collection of foundational font design tokens combined into a preset to define reusable typography.

[Learn more about typography presets](/theme/presets/typography-presets/)

Typography Presets
==================

A collection of foundational font design tokens combined into a preset to define reusable typography.

[Learn more about typography presets](/theme/presets/typography-presets/)