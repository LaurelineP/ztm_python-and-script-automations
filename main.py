# 00 - Introduction & installation code
def run_intro():
	import _00_introduction_and_installations as intro
	# Prompting to let a user interact with the defined logic
	intro.prompt_user()
	print('\n')

	# Text case transformation
	intro.play_with_text('Lowla')
	print('\n')

	# Get time difference
	print(intro.state_date_difference())
	print('\n')


# 01 - Working with files
def run_working_with_file():
	import _01_working_with_files.plain_text


run_intro()
run_working_with_file()
