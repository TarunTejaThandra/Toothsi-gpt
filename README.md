OpenAI GPT-3.5 Demo


This is a simple demo project that demonstrates how to use the OpenAI GPT-3.5 language model for text generation.

Installation

To use this demo, you need to have an OpenAI API key. If you don't have one, you can sign up for a free OpenAI API account and get an API key.

After obtaining an API key, you can clone this repository and install the required dependencies by running:

bash

cd openai-gpt-3.5-demo
pip install -r requirements.txt

Usage

This demo provides two ways of inputting data to the GPT-3.5 model for text generation:

Using a local directory containing plain text files. In this case, you need to create a directory containing one or more plain text files, and specify the path to this directory when running the training.py script. The script will read the text from the files, preprocess it, and use it to train the GPT-3.5 model.

Using Google Docs. In this case, you need to provide the file IDs of one or more Google Docs that you want to use for text generation. The linkingdrive.py script will download the text content of the Google Docs, preprocess it, and use it to generate text using the GPT-3.5 model.

To use the first method, run the training.py script with the --data-dir flag followed by the path to the directory containing the plain text files. For example:

css
python training.py --data-dir /path/to/data/folder
To use the second method, open the linkingdrive.py script and replace the file_ids list with the file IDs of the Google Docs that you want to use. Then run the script using the following command:

python linkingdrive.py
After running either script, you can use the ask_ai() function to generate text using the GPT-3.5 model. This function will prompt you to enter a text prompt, and then use the GPT-3.5 model to generate a continuation of the prompt.

Conclusion
This project provides an easy way to build a Chat GPT chatbot that can be trained on custom data and integrated with Google Sheets. By following the above instructions, you can build your own chatbot and customize it to suit your needs.
