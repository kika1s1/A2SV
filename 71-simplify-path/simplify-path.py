class Solution:
    def simplifyPath(self, path: str) -> str:
        new_path = []
        for folder in path.split('/'):
            if folder!='' and folder!='.' and folder!='..':
                new_path.append(folder) 
            elif folder=='..' and len(new_path)>0:
                    new_path.pop()   
        return '/'+ ('/').join(new_path)