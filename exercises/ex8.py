formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"This ain't a song for the broken-hearted",
	"No silent prayer for the faith-departed",
	"I ain't gonna be just a face in a crowd",
	"You're gonna hear my voice When I shout it out loud"
))
