from bottle import route,request,template,run,Bottle,static_file
from AutoBuild import autoBuild
app = Bottle()

@app.route('/')
def show():
    return template('templates/index')

@app.route('/webBuild/',method='post')
def test():
    return autoBuild()

#下载apk文件
@app.route('/download/:apkname',method = 'get')
def download(apkname):
    print apkname
    return static_file(apkname, root='./project/products/Apks/',download=apkname)

@app.route('/templates/:filename')
def send_static(filename):
    return static_file(filename, root='./templates')

run(app, host='172.20.133.58', port=8080)
