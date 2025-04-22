微博热搜MCP服务
==============

一个简单的微博热搜MCP服务，你可以在Claude AI中使用。本服务提供基础版和高级版两个版本，您可以根据需要选择安装。

功能说明
--------

基础版功能
~~~~~~~~~

基础版MCP服务提供以下功能：

1. **工具(Tool)**: ``get_weibo_hot`` - 获取微博热搜榜前10条内容
2. **资源(Resource)**: ``weibo://hotsearch`` - 提供微博热搜数据作为资源
3. **提示(Prompt)**: ``ask_about_hot_topics`` - 生成关于热门话题的提示

高级版功能
~~~~~~~~~

高级版MCP服务在基础版的基础上，增加了以下功能：

1. **工具(Tool)**:
   - ``get_weibo_hot`` - 获取微博热搜榜前10条内容，并带有日志记录
   - ``get_top_n_hot`` - 获取指定数量的微博热搜条目
   - ``search_hot_topics`` - 搜索包含指定关键词的热搜条目
   - ``get_hot_search_stats`` - 获取热搜统计信息

2. **资源(Resource)**:
   - ``weibo://hotsearch`` - 提供微博热搜数据作为资源
   - ``weibo://hotsearch/{count}`` - 获取指定数量的微博热搜条目

3. **提示(Prompt)**:
   - ``ask_about_hot_topics`` - 生成关于热门话题的提示
   - ``compare_hot_topics`` - 生成比较热门话题的提示

4. **高级特性**:
   - 数据缓存 - 避免频繁请求微博服务器
   - 错误处理 - 更健壮的错误处理机制
   - 进度报告 - 在处理过程中提供进度更新

安装
----

使用pip安装
~~~~~~~~~~

.. code-block:: bash

    pip install weibo-hotsearch-mcp

使用
----

命令行启动
~~~~~~~~~

基础版:

.. code-block:: bash

    weibo-mcp-basic

高级版:

.. code-block:: bash

    weibo-mcp-advanced

或者使用通用命令:

.. code-block:: bash

    # 启动基础版
    weibo-mcp

    # 启动高级版
    weibo-mcp --advanced

在Claude中使用
~~~~~~~~~~~~

安装完成后，MCP服务将自动在Claude Desktop中注册。使用步骤如下：

1. 打开Claude Desktop应用
2. 在对话框中，点击右下角的"+"按钮
3. 在弹出的菜单中选择"微博热搜"或"微博热搜高级版"
4. 现在您可以在对话中使用微博热搜服务了

在CLine插件中配置
~~~~~~~~~~~~~~~

请参考完整文档了解如何在VSCode、JetBrains等IDE的CLine插件中配置。

配置Cookie数据（必需）
~~~~~~~~~~~~~~~~~

必须通过环境变量传递Cookie数据才能正常使用服务:

.. code-block:: bash

    export WEIBO_COOKIE="你的微博Cookie数据"
    weibo-mcp-advanced

注意: 如果未设置 WEIBO_COOKIE 环境变量，服务将无法正常获取微博热搜数据。

许可证
------

本项目采用MIT许可证开源。
