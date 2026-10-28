# PROMPT LOG

## Section 2 - AI Help

I wrote the main code for section 2 by myself. It reads the csv file, groups records by device, calculates the average temperature and error count, filters devices with average temperature above 80 and saves the result in a json file.

After writing the code, I asked AI to help me with some edge cases because I wanted to make the code handle errors better.

The AI suggested some extra checks like:

- Checking if the file exists or not.
- Checking if the file is completely empty.
- Handling the case where the file has a header but no data rows.
- Handling invalid temperature values.
- Avoiding division by zero when calculating average temperature if there are no valid temperature values.

I used these suggestions to improve my code and understand how to handle these cases.

## Section 3 - Chart Generation

## 1. Initial Prompt

I asked the AI to write a Python script that reads my `summary.json` file and uses Matplotlib to create a bar chart comparing the average temperature of each device. I asked it to include a chart title, axis labels, device names, and save the chart as `temperature_chart.png`.

## 2. Follow Up Prompt

Because it's my first time using matplotlib i didn't know what i needed to check, i have not seen what type of graph can be made by this so i didn't know the comparison, so i just asked the ai what can be improved in it and just updated the code

## 3. AI Chat Link
https://chatgpt.com/share/6ae20172-f190-83ec-b654-3ea75939cab4
