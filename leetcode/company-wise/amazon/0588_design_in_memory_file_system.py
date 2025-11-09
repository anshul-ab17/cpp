# LC 588. Design In-Memory File System | Hard | Amazon
class FileSystem:
    def __init__(self):
        self.fs = {'dirs': {}, 'files': {}}

    def _navigate(self, path):
        node = self.fs
        if path == '/': return node
        for part in path.split('/')[1:]:
            if part in node['dirs']: node = node['dirs'][part]
            else: return None
        return node

    def ls(self, path):
        parts = path.split('/'); name = parts[-1]
        parent = self._navigate('/'.join(parts[:-1]) or '/')
        if parent and name in parent.get('files', {}): return [name]
        node = self._navigate(path)
        if not node: return []
        return sorted(list(node['dirs'].keys()) + list(node['files'].keys()))

    def mkdir(self, path):
        node = self.fs
        for part in path.split('/')[1:]:
            if part not in node['dirs']: node['dirs'][part] = {'dirs': {}, 'files': {}}
            node = node['dirs'][part]

    def addContentToFile(self, filePath, content):
        parts = filePath.split('/'); name = parts[-1]
        self.mkdir('/'.join(parts[:-1]) or '/')
        parent = self._navigate('/'.join(parts[:-1]) or '/')
        parent['files'][name] = parent['files'].get(name, '') + content

    def readContentFromFile(self, filePath):
        parts = filePath.split('/'); name = parts[-1]
        parent = self._navigate('/'.join(parts[:-1]) or '/')
        return parent['files'][name]
