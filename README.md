# About
Fng-api is an API for [fakenamegenerator.com](https://fakenamegenerator.com). It has all of the features and customizability as the website does. You can specify gender, age, country, and nameset. The API will scrape the website and parse the data for you.

----

# Usage
Here's an example script to get you started:

```python
from fng_api import *

identity = getIdentity()
print(identity.name)
```

This script will generate a generic identity and print the name. You can specify different arguments in `getIdentity()`. 

```python
getIdentity(nameset=[])
getIdentity(country=[])
getIdentity(gender=str)
getIdentity(minage=str)
getIdentity(maxage=str)
```

## Country
You must pass a list of all of the countries that you would like the identity to possible have to the country argument. Example: 
To generate an identity with information for the countries of either the United States or Brazil, you would write this:

```python
identity = getIdentity(country=["us", "br"])
```

Here is a list of all of the country abbreviations:

- au - Australia
- as - Austria
- bg - Belgium
- br - Brazil
- ca - Canada
- cyen - Cyprus (Anglicized)
- cygk - Cyprus (Greek)
- cz - Czech Republic
- dk - Denmark
- ee - Estonia
- fi - Finland
- fr - France
- gr - Germany
- gl - Greenland
- hu - Hungary
- is - Iceland
- it - Italy
- nl - Netherlands
- nz - New Zealand
- no - Norway
- pl - Poland
- pt - Portugal
- sl - Slovenia
- za - South Africa
- sp - Spain
- sw - Sweden
- sz - Switzerland
- tn - Tunisia
- uk - United Kingdom
- us - United States
- uy - Uruguay

----

## Nameset
You must pass a list of all of the namesets that you would like the identity to possible have to the nameset argument. Example: 
To generate an identity with a name from either a Danish nameset or a French nameset, you would write this:

```python
identity = getIdentity(nameset=["dk", "fr"])
```
Here is a list of all of the nameset abbreviations:

- us - American
- ar - Arabic
- au - Australian
- br - Brazil
- celat - Chechen (Latin)
- ch - Chinese
- zhtw - Traditional Chinese
- hr - Croatian
- cs - Czech
- dk - Danish
- nl - Dutch
- en - England/Wales
- er - Eritrean
- fi - Finnish
- fr - French
- gr - German
- gl - Greenland
- sp - Hispanic
- hobbit - Hobbit
- hu - Hungarian
- is - Icelandic
- ig - Igbo
- it - Italian
- jpja - Japanese
- tlh - Klingon
- ninja - Ninja
- no - Norwegian
- fa - Persian
- pl - Polish
- ru - Russian
- rucyr - Russian (Cyrillic)
- gd - Scottish
- sl - Slovenian
- sw - Swedish
- th - Thai
- vn - Vietnamese

----

## Gender
The gender argument is passed as an integer represented by a string. The integer represents the chance out of 100 that the identity will be a male. So if you wanted the identity to be only a girl, you would set gender equal to 0. If you wanted a 50/50 chance, you would set it to 50. Heres an example of an identity that has a 25% chance to be a male and a 75% chance to be a female:

```python
identity = getIdentity(gender="25")
```

----

## Age Ranges
You can configure the age range of the identity. All you have to do is set the minage and maxage values. Minage cannot be below 0 and maxage cannot be above 100. Minage is also not allowed to be greater than maxage. Here's an example of an identity with the an age range of 15-26:

```python
identity = getIdentity(minage="15", maxage="26")
```

----

## Default Values
Here are the default values for the `getIdentity()` function;

```python
getIdentity(nameset=["us"], country=["us"], gender="50", minage="19", maxage="85")
```

----

# Attributes

You can access an attribute of the identity by doing identity.attribute. So here's how to get the address of an identity as an example:

```python
identity = getIdentity()
print(identity.address)
```

Here's a list of all al the attributes:

- address
- street
- city
- state
- zip
- motherMaidenName
- ssn
- coords
- phone
- countryCode
- birthday
- birthdayMonth
- birthdayDay
- birthdayYear
- age
- zodiac
- email
- username
- password
- website
- useragent
- card
- expiration
- cvv2
- company
- occupation
- height
- heightcm
- weight
- weightkg
- blood
- ups
- westernunion
- moneygram
- color
- vehicle
- guid