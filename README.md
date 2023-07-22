<body>
<h1>Posts App for wordLine company</h1>

<p>The Posts app is a simple application that allows users to manage and view posts. This README file provides instructions on how to set up and run the app.</p>

<h2>Prerequisites</h2>
<p>Before installing the app, ensure you have the following prerequisites:</p>
    <ul>
        <li>Python (>= 3.6)</li>
        <li>Pip (Python package manager)</li>
    </ul>

<h2>Installation</h2>
    <ol>
        <li>Clone the repository to your local machine:</li>
    </ol>
    <pre><code>git clone https://github.com/your_username/posts-app.gitcd posts-app</code></pre>

<ol>
        <li>Set Environment Variable for the Database Password:</li>
    </ol>
    <pre><code>export SQL_PASS='your_db_pass git'</code></pre>


<ol start="3">
    <li>Install Dependencies:</li>
</ol>
    <pre><code>cd backend pip install -r requirements.txt</code></pre>

<ol start="4">
        <li>Run the App in <strong>backend/app</strong> :</li>
</ol>
<pre><code>uvicorn main:app --reload</code></pre>

<h2>Data Structure</h2>
    <p>The app uses the following data structure to represent posts:</p>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Content</th>
        </tr>
        <tr>
            <td>1</td>
            <td>Test Post 1</td>
            <td>&lt;h1&gt;Post 1&lt;/h1&gt;</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Test Post 2</td>
            <td>&lt;h1&gt;Post 2&lt;/h1&gt;</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Test Post 3</td>
            <td>&lt;h1&gt;Post 3&lt;/h1&gt;</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Test Post 4</td>
            <td>&lt;h1&gt;Post 4&lt;/h1&gt;</td>
        </tr>
    </table>

</body>