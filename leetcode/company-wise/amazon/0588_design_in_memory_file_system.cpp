// LC 588. Design In-Memory File System | Hard | Amazon
#include <string>
#include <vector>
#include <map>
#include <sstream>
using namespace std;

class FileSystem {
    struct Dir { map<string, Dir*> dirs; map<string, string> files; };
    Dir* root;
    Dir* navigate(string path) {
        Dir* node = root;
        istringstream ss(path); string part;
        while (getline(ss, part, '/')) if (!part.empty() && node->dirs.count(part)) node = node->dirs[part];
        return node;
    }
public:
    FileSystem() : root(new Dir()) {}
    vector<string> ls(string path) {
        istringstream ss(path); string part; vector<string> parts;
        while (getline(ss, part, '/')) if (!part.empty()) parts.push_back(part);
        Dir* node = root;
        for (int i = 0; i < (int)parts.size()-1; i++) node = node->dirs[parts[i]];
        if (!parts.empty() && node->files.count(parts.back())) return {parts.back()};
        if (!parts.empty() && node->dirs.count(parts.back())) node = node->dirs[parts.back()];
        vector<string> res;
        for (auto& [k,_] : node->dirs) res.push_back(k);
        for (auto& [k,_] : node->files) res.push_back(k);
        sort(res.begin(), res.end()); return res;
    }
    void mkdir(string path) {
        Dir* node = root; istringstream ss(path); string part;
        while (getline(ss, part, '/')) if (!part.empty()) { if (!node->dirs.count(part)) node->dirs[part] = new Dir(); node = node->dirs[part]; }
    }
    void addContentToFile(string filePath, string content) {
        istringstream ss(filePath); string part; vector<string> parts;
        while (getline(ss, part, '/')) if (!part.empty()) parts.push_back(part);
        Dir* node = root;
        for (int i = 0; i < (int)parts.size()-1; i++) { if (!node->dirs.count(parts[i])) node->dirs[parts[i]] = new Dir(); node = node->dirs[parts[i]]; }
        node->files[parts.back()] += content;
    }
    string readContentFromFile(string filePath) {
        istringstream ss(filePath); string part; vector<string> parts;
        while (getline(ss, part, '/')) if (!part.empty()) parts.push_back(part);
        Dir* node = root;
        for (int i = 0; i < (int)parts.size()-1; i++) node = node->dirs[parts[i]];
        return node->files[parts.back()];
    }
};
