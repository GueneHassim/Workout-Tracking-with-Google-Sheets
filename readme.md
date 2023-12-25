The workout tracking code is an exercise that I wrote.
It takes as input the activity I do, written in a human typing style.
The program uses the Nutrixions API, which employs a natural language processing model.
This model understands the activity, duration, length, calories, etc., through the examination of the text.
It then returns a JSON file in response.

From this JSON file, I extract the data I'm interested in.
I use the `datetime` module to capture the current date of the activity registration and the current hour.

{
  "workout": {
    "date": "25/12/2023",
    "time": "10:13:34",
    "exercise": "Swimming",
    "duration": 30,
    "calories": 201,
    "id": 5
  }
}
Then I post them to my Google Sheet using the 'Sheety' API.
after running and pre-debugging the code, I save the sensitive data such as API passkey, ID, Google Sheet endpoint, etc., as environment variables.





