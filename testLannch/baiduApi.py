import urllib.request, requests
import base64
import ssl,sys,json
from PIL import Image

def getAuth():
  # 获取baiduapi access_token
  host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=DEn83iSvMREMfnIE2oIF0wTs&client_secret=yBsoRA27Mcaz5GnYiph4TcSQkGSLKQPd '
  request = urllib.request.Request(host)
  request.add_header('Content-Type', 'application/json; charset=UTF-8')
  response = urllib.request.urlopen(request)
  content = response.read()
  if (content):
    access_token = json.loads(content.decode())['access_token']
    # print(json.loads(content.decode()))
  return str(access_token)

def makeImage(srcImgPath, cutImgPath):
  # 处理图片 -- 返回处理后的图片路径
  image = Image.open(srcImgPath) 
  # 1.灰白化
  imgry = image.convert("L")
  threshold = 140
  table = []
  for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
  img = imgry.point(table, '1')
  # img.show()

  # 2.原图裁剪 -- 返回裁剪后图片的路径
  x = 402 # 距离裁剪图片的坐标x
  y = 238 # 距离裁剪图片的坐标y
  w = 262 # 裁剪图片的宽度
  h = 75  # 裁剪图片的高度
  out = img.crop((x, y, x+w, y+h))
  out.save(cutImgPath)  # 裁剪后的位置
  return cutImgPath

def getImageWord(imgPath):
  # 调用baiduapi
  url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic'  
  data = {}  
  data['access_token']=getAuth()

  # 读取图片  
  file = open(imgPath,'rb')  
  img = file.read()  
  file.close()  

  # 传递baidu-api参数
  data['image'] = base64.b64encode(img)  
  headers={
      "Content-Type":"application/x-www-form-urlencoded",
      "apikey":"15180314"
  }
  res = requests.post(url=url, headers=headers, data=data)
  result = res.json()

  # 返回识别图片后的文本
  # print('返回识别图片后的文本:',result)  
  return result

def makeLannchNum(text):
  # 处理识别后的文本
  if(text['words_result_num']==0):
    # 识别结果为空
    print('baiduApi picture ocr is null:\n',text)
    return
  else:
    # 处理图片识别的结果 -- 错误将9 --> q|Q, 7-->ㄇ，包含乘号‘X’
    num = list(text['words_result'][0]['words'])
    # 删除乘号 
    if(num[1]==('×' or "X")):
      del num[1]

    for i in range(0, len(num)):
      if(num[i]==("G" or "q" or 'Q')):
        num[i] = '9'
      elif(num[i]=='ㄇ'):
        num[i]='7'
    # 计算结果
    try:
      result =  int(num[0])*int(num[1])
      results = []
      A = int(result/10)
      B = result%10
      results.append(A)
      results.append(B)
    except ValueError as e:
      print(e)
    print(result)
    return results

if __name__ == '__main__':
  # 设置裁剪图片的路径
  srcImgPath = r'D://test_image/number.png'
  cutImgPath = r'D://test_image/copy_num.png'# copy_num

  text = getImageWord(makeImage(srcImgPath, cutImgPath))
  # text = getImageWord(cutImgPath) # 测试识别图片
  # print("baduapi:",text)
  makeLannchNum(text)