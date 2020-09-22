#


simple terminal interface to make it fast and simple to store insuline intake, making the process less tedious.

basically -& bs 4 -m snickers
^
would call the program, make an entry into storage,
The entry would contain the insuline dose in the relevant unit, 4 of them in this case
It would get a timestamp, for when it was entered, or when the insuline was injected

It would have the possibility to add a comment, or a message,
in this case, indicated with "-m" and containing "snickers"
But for future-proofing, it needs to be in a way that makes sure
the message can be handled by something else before being stored.
Something should be allowed to process the message before it is stored
some kind of processing pipeline.


later:
Add a way of storing information about food and snacks you eat,
creating aliases for datamodels, ie if i have a snickers,
it would relate to data i have added using another module.
And if i add snickers as a message when making an entry,
it would add some kind of link, relationship to the corresponding
data if existing.
