# -*- coding:utf-8 -*-
#基础函数
class Functor:
	"""
	构造任意参数的CallBack函数类
		@ivar _fn:	CallBack函数
		@type _fn:	function
		@ivar _fn:	参数
		@type _args:	tuple
	"""
	
	def __init__(self,fn,*args):
	"""
	构造函数
		@param fn:	CallBakc函数
		@type fn:	function
		@param args: 	参数
		@type args:	tuple
	"""
		self._fn=fn
		self._args=args
		self.m_type=""
	def __call__(self,*args):
	"""
	调用CallBack函数fn
		@param args: 	参数
		@type args:	tuple
		@return: 	CallBack函数的返回值
	"""
	return self._fn(*(self._args+args))
	def Type(self):
		return self.m_Type
	def SetType(self,a):
		self.m_Type=a



def GetTraceText(*args):
    import traceback
    txtlist=[]
    txtlist.append("----------------------")
    stack=traceback.extract_stack()
    for filename,lineno,name,line in stack[:-1]:   
        txt=" File '%s', line, %s, in '%s'"%(filename,lineno,name)
        txtlist.append(txt)
    if args:
        txt="其他信息:"
        for s in args:
            txt="%s%s,"%(txt,s)
        txt=txt[:-1]
        txtlist.append(txt)
     return txtlist

def TraceMsg(*args):
    txtlist=GetTraceText(*args)
    for txt in txtlist:
        print (txt)

        


