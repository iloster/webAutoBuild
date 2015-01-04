from bottle import route,request,template,run,Bottle,static_file
from AutoBuild import autoBuild
from Flag import createFlag,deleteFlag,checkFlag
from GetApkInfo import getApkInfo
from ParseXml import parseXmlString
app = Bottle()

@app.route('/')
def show():
    apkInfo = getApkInfo();
    return template('templates/index',apkInfo = apkInfo)

@app.route('/parsexml')
def parseXml():
    return template('templates/parseXml',xmlresults1 = ['',''])

@app.route('/upload', method = 'POST')
def do_upload():
    name = request.forms.get('name')
    data = request.files.get('data')
    print name,data
    if name and data:
        raw = data.file.read() # 这对于大文件来说是很危险的    
        #print raw
        xmlresults,xmlresultsTag = parseXmlString(raw)
        filename = data.filename
        #return "a %s! a %s (%d k)." % (name, filename, len(raw))
        xmlresults1 = [xmlresults,xmlresultsTag]
        #print xmlresults1
        return template('templates/parseXml',xmlresults1 = [xmlresults,xmlresultsTag,name])
    return "文件和类名不能为空!"

@app.route('/webBuild/:appid/:gametype/:channel/:versionName',method='post')
def test(appid,gametype,channel,versionName):
    if checkFlag():
        return {"ret":-1}
    else:
        createFlag()
        print appid,gametype,channel
        result = autoBuild(appid,gametype,channel,versionName)
        deleteFlag()
        return result

#下载apk文件
@app.route('/download/:nowTime/:apkname',method = 'get')
def download(nowTime,apkname):
    print apkname
    
    return static_file(apkname, root='./project/products/Apks/'+nowTime,download=apkname)

@app.route('/templates/:filename')
def send_static_index(filename):
    return static_file(filename, root='./templates')

@app.route('/templates/js/:filename')
def send_static_js(filename):
    return static_file(filename, root='./templates/js')

@app.route('/templates/css/:filename')
def send_static_css(filename):
    return static_file(filename, root='./templates/css')

@app.route('/templates/fonts/lato/:filename')
def send_static_font(filename):
    return static_file(filename, root='./templates/fonts/lato')

@app.route('/templates/fonts/glyphicons/:filename')
def send_static_glyphicons(filename):
    return static_file(filename, root='./templates/fonts/glyphicons')


run(app, host='172.20.154.35', port=8080)
#run(app)
