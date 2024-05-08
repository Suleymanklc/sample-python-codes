import requests
import base64
import json

personal_access_token = 'xxx'
build_api_organization_url = 'https://dev.azure.com/xxx/'
release_api_organization_url = 'https://vsrm.dev.azure.com/xxx/'
project_name = 'xxx'
repo_id = 'xxx'  


class FindForBuildPipelines:
    def __init__(self):
        self.personal_access_token = personal_access_token
        self.build_api_organization_url = build_api_organization_url
        self.project_name = project_name
        self.repo_id = repo_id

    def get_project_id(self):
        url = build_api_organization_url + '/_apis/projects/'
        headers = {
            'Authorization': 'Basic ' + base64.b64encode(b':' + self.personal_access_token.encode()).decode(),
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        projects = response.json()['value']
        for project in projects:
            if project['name'] == project_name:
                return project['id']
        return None

    def list_pipelines(self):
        if not self.get_project_id():
            print("Project not found.")
            return
        url = build_api_organization_url + self.get_project_id() + '/_apis/pipelines?api-version=6.0-preview.1'
        headers = {
            'Authorization': 'Basic ' + base64.b64encode(b':' + self.personal_access_token.encode()).decode(),
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        pipelines = response.json()['value']
        return pipelines

    def find_pipelines_using_repo(self, repo_id):
        pipelines_using_repo = []
        for pipeline in self.list_pipelines():
            href_url = pipeline['_links']["self"]["href"]

            headers = {
                'Authorization': 'Basic ' + base64.b64encode(b':' + self.personal_access_token.encode()).decode(),
                'Content-Type': 'application/json'
            }
            response = requests.get(href_url, headers=headers)
            response.raise_for_status()
            data = response.json()
            if json.dumps(data).__contains__(repo_id):
                print(pipeline['_links']["web"]["href"])
        return pipelines_using_repo


class FindReposForReleases:
    def __init__(self):
        self.personal_access_token = personal_access_token
        self.release_api_organization_url = release_api_organization_url
        self.project_name = project_name
        self.repo_id = repo_id

    def list_pipelines(self):
        url = release_api_organization_url + self.project_name + '/_apis/release/releases?api-version=7.1-preview.8'
        headers = {
            'Authorization': 'Basic ' + base64.b64encode(b':' + self.personal_access_token.encode()).decode(),
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        releases = response.json()['value']
        return releases

    def find_releases_using_repo(self, repo_id):
        pipelines_using_repo = []
        for pipeline in self.list_pipelines():
            href_url = pipeline['_links']["self"]["href"]

            headers = {
                'Authorization': 'Basic ' + base64.b64encode(b':' + self.personal_access_token.encode()).decode(),
                'Content-Type': 'application/json'
            }
            response = requests.get(href_url, headers=headers)
            response.raise_for_status()
            data = response.json()
            if json.dumps(data).__contains__(repo_id):
                print(pipeline['_links']["web"]["href"])
        return pipelines_using_repo


findForBuildPipelines = FindForBuildPipelines()
findForBuildPipelines.find_pipelines_using_repo(repo_id)

findReposForReleases = FindReposForReleases()
findReposForReleases.find_releases_using_repo(repo_id)

