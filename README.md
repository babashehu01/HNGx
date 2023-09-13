Backend Stage One Task README

**Welcome to the README for the "Backend Stage One Task."** In this task, you will create and host an endpoint that accepts GET requests with specific query parameters and returns information in JSON format. Below are the details and requirements for the task.

## Objective

The objective of this task is to create and host an endpoint using any programming language of your choice. This endpoint should take two GET request query parameters and return specific information in JSON format.

## Requirements

The information that your endpoint should provide includes the following data points:

- **Slack name**
- **Current day of the week**
- **Current UTC time** (with validation of +/-2 minutes)
- **Track**
- The **GitHub URL of the file being run**
- The **GitHub URL of the full source code**
- A **status code of success (HTTP 200)**

Here is the JSON format that your endpoint should adhere to:

```json
{
  "slack_name": "example_name",
  "current_day": "Monday",
  "utc_time": "2023-08-21T15:04:05Z",
  "track": "backend",
  "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
  "github_repo_url": "https://github.com/username/repo",
  "status_code": 200
}
