from bottle import route,request,template,run,Bottle,static_file
from AutoBuild import autoBuild
from Flag import createFlag,deleteFlag,checkFlag
app = Bottle()

@app.route('/')
def show():
    return template('templates/index')

@app.route('/webBuild/',method='post')
def test():
    if checkFlag():
        return {"ret":-1}
    else:
        createFlag()
        result = autoBuild()
        deleteFlag()
        return result

#下载apk文件
@app.route('/download/:apkname',method = 'get')
def download(apkname):
    print apkname
    
    return static_file(apkname, root='./project/products/Apks/',download=apkname)

@app.route('/templates/:filename')
def send_static(filename):
    return static_file(filename, root='./templates')

run(app, host='172.20.133.58', port=8080)
#run(app)
