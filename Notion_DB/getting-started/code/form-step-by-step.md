Form step-by-step | NewsKit design system

Guides

Form step-by-step
=================

Step-by-step guide for engineers to build a form using the form subcomponents.

Key benefits:
-------------

*   Dynamic
    
*   Subcomponents give more freedom on styling the form etc
    
*   Ability to put together different form inputs easily
    

The [form](/components/form/) is a non-visual component. It is made up of several subcomponents, which together display the visuals of the form alongside validation and rules. These rules let the user know what input is required from them.

* * *

Basic form layout
-----------------

Let’s start off with a basic form layout.

With the example above, the component structure is:

    1<Form onSubmit={onSubmit}>
    2  <FormInput
    3      name="email-valid"
    4      rules={{
    5      required: 'Required field',
    6      pattern: {
    7          value: /^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i,
    8          message: 'Please provide a valid email address',
    9      },
    10      }}
    11  >
    12      <FormInputLabel>Email address</FormInputLabel>
    13      <FormInputTextField />
    14      <FormInputAssistiveText>Eg. yourname@gmail.com</FormInputAssistiveText>
    15  </FormInput>
    16  <Button type="submit">Submit</Button>
    17</Form>

Validation comes from the `<Form>`. All subcomponents need to be wrapped inside the `<Form />` in order for it to be validated.  
  
`<FormInput>` is where you set your rules for the input and the pattern. The above example requires an email. All subcomponents need to be wrapped inside `<FormInput />` in order for the rules to work, and for the validation to be passed down to the other components such as the `<FormInputTextField />` and the `<FormInputAssistiveText />`.

You can also add a message, e.g.  
`message: 'Please provide a valid email'`, which pops up if the user provides an incorrect input.  
  
`<FormInputLabel />` is an optional component that can be placed wherever needed. In the instance above we place it above the input field. You can also style the label to inherit the same state colour as the [text field](/components/text-field/) and assistive text.  
  
`<FormInputTextField />` is where the user inputs text. It also comes with start and end icons called `startEnhancer` and `endEnhancer`, which are both optional.  
  
`<FormInputAssistiveText />` is an optional component. If placed inside `<FormInput />`, the validation will be passed down to it so it changes colour accordingly. If you provided a message in `<FormInput />` it will be displayed here for the user (as seen in the image above).

### Props

`<FormInput />` and its subcomponents all come with size props `small | medium | large`.  
  
A user can also force states on all such as `valid | invalid | disabled`.

* * *

Other FormInput components
--------------------------

Above, we showed you `<FormInput />` with a `<FormInputTextField />`.  
  
We also have `<FormInputSelect/>`, `<FormInputCheckbox />`, and `<FormInputRadioButton />`.  
  
Below is an example of `<FormInputSelect />` being wrapped inside `<FormInput />`.

### FormInputSelect component

This has the same structure as the basic Form example with an input field.  
  
Again, `<FormInput />` has components wrapped inside it, and you can set rules. The same optional `<FormInputLabel />`, and `<FormInputAssistiveText />` can be added in as well.  
  
Here, we are using `<FormInputSelect />`, which comes with an optional `startEnhancer` and `endEnhancer`.  
  
Inside `<FormInputSelect />` you can add in `<SelectOption />`, which comes from the [select](/components/select/) component.

    1<Form onSubmit={onSubmit}>
    2    <FormInput name="subscription-package">
    3        <FormInputLabel>Subscription package</FormInputLabel>
    4        <FormInputSelect>
    5          <SelectOption value="digital-only">Digital only</SelectOption>
    6          <SelectOption value="print-only">Print only</SelectOption>
    7          <SelectOption value="print-and-digital">Print + Digital</SelectOption>
    8        </FormInputSelect>
    9    </FormInput>
    10    <Button type="submit">Submit</Button>
    11</Form>

### FormInputCheckbox component

This has the same structure as the basic form example with an input field.  
  
Again, `<FormInput />` has components wrapped inside it, and you can set rules. The same optional `<FormInputLabel />` and `<FormInputAssistiveText />` can be added in as well.  
  
But now, we are using `<FormInputCheckbox />`, which comes with prop label. This is for the text that is placed next to the [checkbox](/components/checkbox/) component.

    1<Form onSubmit={onSubmit}>
    2    <Fieldset legend="Terms and conditions">
    3        <FormInput
    4            name="terms"
    5            rules={{
    6                required: 'Please accept the terms',
    7            }}
    8        >
    9            <FormInputCheckbox label="I accept the terms" value="tc" />
    10            <FormInputAssistiveText validationIcon />
    11        </FormInput>
    12    </Fieldset>
    13    <Button type="submit">Submit</Button>
    14</Form>

### FormInputRadioButton component

This has the same structure as the basic form example with an input field.  
  
Again, `<FormInput />` has components wrapped inside it, and you can set rules. The same optional `<FormInputLabel />` and `<FormInputAssistiveText />` can be added in as well.  
  
But now, we are using `<FormRadioButtutton />`. This component should be wrapped inside a `<Fieldset>`. We use the [fieldset](/components/fieldset/) component to group related form inputs.  
  
We are also using `<RadioGroup />`. A [radio group](/components/radio-button/) is defined by giving each of the radio buttons in the group the same name. Once a radio group is established, selecting any radio button in that group automatically deselects any currently-selected radio button in the same group.

    1<Form onSubmit={onSubmit}>
    2    <Fieldset legend="Pick one interest">
    3      <RadioGroup>
    4        {['Reading', 'Hiking', 'Cooking'].map(value => (
    5          <FormInput key={value} name="interest" rules={{required: 'Please select an option'}}>
    6            <FormInputRadioButton
    7              label={value}
    8              value={value}
    9              overrides={{spaceStack: 'space030'}}
    10            />
    11          </FormInput>
    12        ))}
    13      </RadioGroup>
    14      <FormInput name="interest" rules={{required: 'Please select an option'}}>
    15        <FormInputAssistiveText validationIcon />
    16      </FormInput>
    17    </Fieldset>
    18    <Button type="submit">Submit</Button>
    19 </Form>

* * *

Combined form
-------------

Below is an example of the [form](/components/form/) with different inputs within a [fieldset](/components/fieldset/) which is used when grouping together related form components.  
  
This form is made up of `<FormInputTextField />`, `<FormInputRadioButton />`, and `<FormInputCheckbox />`.

    1<Form onSubmit={onSubmit}>
    2    <FormInput
    3      name="email-valid"
    4      rules={{
    5        required: 'Required field',
    6        pattern: {
    7          value: /^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i,
    8          message: 'Please provide a valid email address',
    9        },
    10      }}
    11    >
    12      <FormInputLabel>Email address</FormInputLabel>
    13      <FormInputTextField />
    14      <FormInputAssistiveText>Eg. yourname@gmail.com</FormInputAssistiveText>
    15    </FormInput>
    16
    17
    18    <Fieldset legend="Pick one interest">
    19      <RadioGroup>
    20        {['Reading', 'Hiking', 'Cooking'].map(value => (
    21          <FormInput
    22            key={value}
    23            name="interest"
    24            rules={{required: 'Please select an option'}}
    25          >
    26            <FormInputRadioButton
    27              label={value}
    28              value={value}
    29            />
    30          </FormInput>
    31        ))}
    32      </RadioGroup>
    33      <FormInput name="interest" rules={{required: 'Please select an option'}}>
    34        <FormInputAssistiveText validationIcon />
    35      </FormInput>
    36    </Fieldset>
    37
    38
    39    <Fieldset legend="Terms and conditions">
    40      <FormInput
    41        name="terms"
    42        rules={{
    43          required: 'Please accept the terms',
    44        }}
    45      >
    46        <FormInputCheckbox label="I accept the terms" value="tc" />
    47        <FormInputAssistiveText validationIcon />
    48      </FormInput>
    49    </Fieldset>
    50
    51    <Button type="submit">Submit</Button>
    52  </Form>

As you can see, each of the components mentioned is wrapped inside its own `<FormInput />`, so we can set the rules for each.  
  
Below you can see that the user won’t be able to submit unless the input field has the correct data.

Now that everything has been entered correctly you can see that every component is valid and the user can proceed.

* * *

Need Help?
==========

Can’t find what you’re looking for?

[Get in touch](/about/contact-us/)

Need Help?
==========

Can’t find what you’re looking for?

[Get in touch](/about/contact-us/)