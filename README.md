# Lambda-WebApp-Dynamodb-S3
This repository contains the necessary code and configuration files to develop and deploy an interactive web app using AWS Lambda, API Gateway, DynamoDB, and S3 for static web hosting.
## Getting Started
Follow the steps below to set up and deploy the web application:
## Files
1. lambda_function.py: This file contains the AWS Lambda function code in Python. It handles the registration process and sends a confirmation email to the user.
```
<lambda_function.py>
```
[Get the file 'Lambda_function.py' Here](https://github.com/aduome/Lambda-WebApp-Dynamodb-S3/blob/main/lambda_function.py)

2. index.html: This file represents the main HTML page of the web app. It includes a registration form where users can enter their details and submit the form to register.
```
<index.html>
```
[Get the file 'index.html' Here](https://github.com/aduome/Lambda-WebApp-Dynamodb-S3/blob/main/index.html)

3. error.html: This file represents the error page displayed when an issue with the web app exists.
```
<error.html>
```
[Get the file 'error.html' Here](https://github.com/aduome/Lambda-WebApp-Dynamodb-S3/blob/main/error.html)

4. lambda-role-policy.json: This JSON file contains the IAM policy that needs to be attached to the Lambda function's execution role. It provides the necessary permissions to access the DynamoDB table.
```
<lambda-role-policy.json>
```
[Get the file 'lambda_role_policy' Here](https://github.com/aduome/Lambda-WebApp-Dynamodb-S3/blob/main/lambda_policy.txt)
## Prerequisites
Before deploying the web app, make sure you have the following prerequisites:

- An AWS account with appropriate permissions to create Lambda functions, API Gateway, DynamoDB tables, and S3 buckets.
- AWS CLI installed and configured with your AWS account credentials.
- Python and pip installed on your development machine.

## Architecture
The application architecture is based on the following AWS services:

- AWS Lambda: Provides serverless compute for running backend functions.
- API Gateway: Exposes RESTful APIs for frontend communication with backend services.
- DynamoDB: A NoSQL database for storing and retrieving data.
- S3: Used for hosting the static frontend files.

![Get the file 'error.html' Here](https://aws.amazon.com/lambda/)

## Deployment Steps
Follow these steps to deploy the interactive web app:

1. Create a new DynamoDB table named 'table name' in the desired AWS region.
2. Update the lambda_function.py file with your DynamoDB table name and any other customization required for your application.
3. Create an execution role for your Lambda function and attach the lambda-role-policy.json policy to it. Make sure the role has the necessary permissions to access DynamoDB.
4. Deploy the Lambda function using the AWS CLI or AWS Management Console.
5. Create an API Gateway REST API and configure it to use a Lambda proxy integration with the deployed Lambda function.
6. Deploy the API Gateway API and make note of the API endpoint URL.
7. Create an S3 bucket and configure it for static website hosting.
8. Upload the index.html and error.html files to the S3 bucket.
9. Enable public access to the uploaded files in the S3 bucket.
10. Visit the S3 bucket URL in a web browser to access the deployed web app.

## Conclusion
You can now customize the web app further or add additional features as per your requirements.
If you encounter any issues or have questions, please refer to the official AWS documentation or reach out for support.

<!-- CONTACT -->

## Contact

Daniel Agyei - [@my_linkedin](https://www.linkedin.com/in/daniel-owusu-banahene-agyei)

Email: [My Email](daniel.agyeibanahene@gmail.com)

Project Link: [Project Link](https://github.com/aduome/Lambda-WebApp-Dynamodb-S3/edit/main))

## Contributing

Contributions are welcome! If you find any issues or want to enhance the functionality, feel free to open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Resources

- [AWS Lambda Documentation](https://aws.amazon.com/lambda/)
- [AWS API Gateway Documentation](https://aws.amazon.com/api-gateway/)
- [AWS DynamoDB Documentation](https://aws.amazon.com/dynamodb/)
- [AWS S3 Documentation](https://aws.amazon.com/s3/)
- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Amazon SES Documentation](https://aws.amazon.com/ses/)
