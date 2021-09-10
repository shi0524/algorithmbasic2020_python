# -*- coding: utf-8 –*-

"""
给定一棵二叉树的头节点head
求以head为头的树中，最小深度是多少？

morris遍历
    判断高度: 1、当前节点是前一节点的子树
             2、前一节点是当前节点的左子树最右子树（第二次来到时, 前一节点的高度 - 当前节点到前一节点距离）
    判断叶节点: 第二次来到节点, 还原左子树最右子树的右指针, 判断左子树最右子树是否是叶节点
"""
