  Object Re(self)lations Practice Code Challenge - Magazines

## Introduction

For this assignment, we'll be working with a Magazine domain.

We have three models: `Magazine`, `Subscription`, and `Reader`.

For our purposes, a `Magazine` has many `Subscription`s, a `Reader` has many `Subscription`s, and a `Subscription` belongs to a `Magazine` and to an `Reader`.

`Magazine` - `Reader` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed in a suggested order, but you can feel free to tackle the ones you think are easiest. Be careful: some of the later methods rely on earlier ones.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You can add code to the `debug.py` file to define variables and create sample
instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First, prioritize getting things working. Then, if there is time at the end, refactor your code to adhere to best practices. When you encounter duplicated logic, extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to build out any helper methods if needed.

_Where would you place a class variable all = [] to act as a Single Source of Truth?_
 
### Initializers and Properties

#### Magazine
- `Magazine __init__(self, title)`
   - Magazine should be initialized with a title
- `Magazine property title`
   - should return the magazine's title
   - title must be a string
   - the title cannot be changed after initialzation

#### Reader
- `Reader __init__(self, name, email)`
   - Reader should be initialized with a name and an email
- `Reader property name`
   - should return the readers name
   - cannot be an empty string
- `Reader property email`
   - should return the readers email
   - cannot be an empty string

#### Subscription
- `Subscription __init__(self, magazine, reader, price)`
   - Subscription should be initialized with a magazine, reader, and a price
- `Subscription property reader(self)`
  - should return the `Reader` instance for this subscription
  - must be of type `Reader`
  - `raise Exeption` if setter fails
- `Subscription magazine(self)`
  - should return the `Magazine` instance for this subscription
  - must be of type `Reader`
  - `raise Exeption` if setter fails
- `Subscription property price(self)`
  - should return the price of the subscription as a 2-decimal float
  - must be floats between 1.00 and 49.99 inclusive
  - `raise Exeption` if setter fails

### Object Relationship Methods

#### Magazine
- `Magazine subscriptions(self)`
  - returns a list of all `Subscription` instances for this magazine
- `Magazine readers(self)`
  - returns a list of all `Reader` instances who are subscribed to this magazine

#### Reader
- `Reader subscriptions(self)`
  - should return a list of all `Subscription` instances for this reader
- `Reader magazines(self)`
  - should return a list of all `Magazine` instances that this reader is subscribed to


### Aggregate and Association Methods

#### Subscription
- `Subscription print_details(self)`
  - `prints` a string to the terminal to display the details of the subscription
  - the string should be formatted like this: `{reader name} subscribed to {magazine title} for ${subscription price}`

#### Reader
- `Reader subscribe(self, magazine, price)`
  - takes a `magazine` (an instance of the `Magazine` class) and a `price` (integer) as arguments, and creates a new `subscription` associated with the magazine and the reader
- `Reader total_subcription_price(self)`
  - returns the total price for all the reader's subscriptions
- `Reader cancel_subscription(magazine)`
  - takes a `magazine` instance and removes the subscription for this reader
  - what change would you need to make on the Subscription class for this to work?

#### Magazine

- `Magazine email_list(self)`
  - returns a `String` of a semi-colon separated list of emails for all the readers subscribed to this magazine
  - the string should be formatted like this: `email1@example.com;email2@example.com;email3@example.com`
- `Magazine classmethod most_popular(cls)`
  - returns the `Magazine` instance with the most subscribers