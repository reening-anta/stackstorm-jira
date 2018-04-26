from lib.base import BaseJiraAction

__all__ = [
    'UpdateJiraIssueAction'
]


class UpdateJiraIssueAction(BaseJiraAction):

    def run(self, issue_key, fields):
        issue = self._client.issue(issue_key)
        result = issue.update(fields=fields)

        return result
