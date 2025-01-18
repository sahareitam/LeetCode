/**
* Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    unordered_map<int,int> inordermap;
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        for (int i = 0; i < inorder.size(); i++) {
            inordermap[inorder[i]] = i;
        }
        return helper_build(preorder,inorder,0,0,inorder.size()-1);
    }
    TreeNode* helper_build(vector<int>& preorder, vector<int>& inorder,int preStart,int inStart,int inEnd)
    {
        if(preStart >= preorder.size() || inStart > inEnd)
        {
            return nullptr;
        }
        TreeNode* root = new TreeNode(preorder[preStart]);

        int rootindex = inordermap[preorder[preStart]];
        int numleft = rootindex-inStart;

        root->left = helper_build(preorder, inorder,preStart + 1,inStart,rootindex-1);

        root->right = helper_build(preorder, inorder,preStart + numleft + 1,rootindex + 1,inEnd);

        return root;
    }


};