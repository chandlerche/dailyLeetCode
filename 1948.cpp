class FolderIndices {
public:
    int index;
    unordered_map<string, int> folderIndices;
    unordered_map<int, string> indexFolders;

    FolderIndices() : index(0) {}

    int getIndex(string& folder) {
        auto iter = folderIndices.find(folder);
        if (iter == folderIndices.end()) {
            ++index;
            folderIndices[folder] = index;
            indexFolders[index] = folder;
            return index;
        }
        else {
            return iter->second;
        }
    }

    string getFolder(int index) {
        return indexFolders[index];
    }
};

class Node {
public:
    int index;
    bool needDelete;
    map<int, Node*> children;

    Node() : index(0), needDelete(false){}
    Node(int _index) : index(_index), needDelete(false) {}
};

class Tree {
public:
    Node* root;
    FolderIndices* folderIndices;
    unordered_map<string, Node*> hashTrees;

    Tree(FolderIndices* _folderIndices) {
        folderIndices = _folderIndices;
        root = new Node;
    }

    void buildTree(vector<vector<string>>& paths) {
        for (auto& path : paths) {
            insert(path);
        }
    }

    void insert(vector<string>& path) {
        Node* current = root;

        for (auto& folder : path) {
            int index = folderIndices->getIndex(folder);
            auto iter = current->children.find(index);
            if (iter == current->children.end()) {
                Node* node = new Node(index);
                current->children[index] = node;
                current = node;
            }
            else {
                current = iter->second;
            }
        }
    }

    string DFS4FindSame(Node* node) {
        string hashTree;

        if (!node->children.empty()) {
            for (auto iter = node->children.begin(); iter != node->children.end(); ++iter) {
                hashTree += "C";
                hashTree += DFS4FindSame(iter->second);
            }

            auto iter = hashTrees.find(hashTree);
            if (iter != hashTrees.end()) {
                iter->second->needDelete = true;
                node->needDelete = true;
            }
            else {
                hashTrees[hashTree] = node;
            }
        }

        return hashTree + "S" + to_string(node->index);
    }

    void DFS4DeleteNode(Node* node) {
        auto iter = node->children.begin();

        while (iter != node->children.end()) {
            if (iter->second->needDelete) {
                iter = node->children.erase(iter);
            }
            else {
                DFS4DeleteNode(iter->second);
                ++iter;
            }
        }
    }

    void DFS4GetFolders(Node* node, vector<string>& path, vector<vector<string>>& folderLeft) {
        if (node != root) {
            string folder = folderIndices->getFolder(node->index);
            path.push_back(folder);
            folderLeft.push_back(path);
        }

        for (auto iter = node->children.begin(); iter != node->children.end(); ++iter) {
            DFS4GetFolders(iter->second, path, folderLeft);
        }

        if (node != root) {
            path.pop_back();
        }
    }
};

class Solution {
public:
    vector<vector<string>> deleteDuplicateFolder(vector<vector<string>>& paths) {
        FolderIndices folderIndices;
        Tree tree(&folderIndices);
        vector<string> path;
        vector<vector<string>> folderLeft;

        tree.buildTree(paths);
        (void)tree.DFS4FindSame(tree.root);
        tree.DFS4DeleteNode(tree.root);
        tree.DFS4GetFolders(tree.root, path, folderLeft);

        return folderLeft;
    }
};
