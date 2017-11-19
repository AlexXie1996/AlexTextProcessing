# coding=utf-8  

import os
import wx
from model.my_model import *

class KeyWordsPanel(wx.Panel):
	"""
	"""
	def __init__(self, parent, model):
		"""
		"""
		wx.Panel.__init__(self, parent) 
		self.model = model
		self.rekey = []
		self.resent = ""

		# input sentence
		self.lbgets = wx.StaticText(self, label="input a sentence here:", pos=(20, 10))
		self.sentence = wx.TextCtrl(self, pos=(20, 40), size=(280, 150), style=wx.TE_MULTILINE)
		self.Bind(wx.EVT_TEXT, self.EvtSentence, self.sentence)

		# comboBox  
		self.numlist = ['5', '7', '10', '20']  
		self.lblselnum = wx.StaticText(self, label="Select keywords num:", pos=(30, 205))    
		self.boxselnum = wx.ComboBox(self, pos=(190, 200), size=(95, -1),choices=self.numlist,style=wx.CB_DROPDOWN)
		self.boxselnum.SetSelection(0)
		self.keynums = int(self.numlist[0])
		self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.boxselnum)  

		# button1
		self.button1 = wx.Button(self, label="Execute", pos=(330, 215))  
		self.Bind(wx.EVT_BUTTON, self.OnclickButton1, self.button1)  		

		# button2
		self.button2 = wx.Button(self, label="Save", pos=(430, 215))  
		self.Bind(wx.EVT_BUTTON, self.OnclickButton2, self.button2)

		# result
		self.lbresult = wx.StaticText(self, label="top x keys :", pos=(340, 10))
		self.result = wx.TextCtrl(self, pos=(330, 30), size=(340, 175), style=wx.TE_MULTILINE | 										wx.TE_READONLY)

	def EvtSentence(self, event):
		"""
		"""
		self.resent = event.GetString()

	def EvtComboBox(self, event):
		"""
		"""
		self.keynums = int(self.numlist[event.GetInt()])

	def OnclickButton1(self, event):
		"""
		"""
		self.result.Clear()
		self.rekey = self.model.keywords(self.resent)
		
		for i in range(self.keynums):
			try:
				self.result.AppendText('keyword%d: %s\n' %(i+1, 
								self.rekey[i][0]))		
			except:
				self.result.AppendText('keyword%d: %s\n' %(i+1, ""))

	def OnclickButton2(self, event):
		"""
		"""
		with open('keywords', 'w') as f:
			for key in self.rekey:
				f.write("key: %s  value: %f\n" %(key[0], key[1]))

class RelativeWordsPanel(wx.Panel):
	"""
	"""
	def __init__(self, parent, model):
		"""
		"""		
		wx.Panel.__init__(self, parent)  
		self.model = model
		self.rekey = []
		self.reword = ""

		# input sentence
		self.lbgets = wx.StaticText(self, label="input a word here:", pos=(20, 40))
		self.word = wx.TextCtrl(self, pos=(20, 60), value="输入一个词", size=(250, 50))
		self.Bind(wx.EVT_TEXT, self.EvtWord, self.word)

		# comboBox  
		self.numlist = ['5', '7', '10', '20']  
		self.lblselnum = wx.StaticText(self, label="Select relatives num:", pos=(20, 125))    
		self.boxselnum = wx.ComboBox(self, pos=(175, 120), size=(95, -1), choices=self.numlist,style=wx.CB_DROPDOWN)  		
		self.boxselnum.SetSelection(0)
		self.keynums = int(self.numlist[0])
		self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.boxselnum)  

		# hint
		self.lbhint1 = wx.StaticText(self, label="Hint:", pos=(20, 160))
		self.lbhint2 = wx.StaticText(self, label="Please be patient as this may", pos=(20, 180))
		self.lbhint3 = wx.StaticText(self, label="take some time", pos=(20, 200))
		# button1
		self.button1 = wx.Button(self, label="Execute", pos=(330, 215))  
		self.Bind(wx.EVT_BUTTON, self.OnclickButton1, self.button1)  		

		# button2
		self.button2 = wx.Button(self, label="Save", pos=(430, 215))  
		self.Bind(wx.EVT_BUTTON, self.OnclickButton2, self.button2)

		# result
		self.lbresult = wx.StaticText(self, label="top x relatives :", pos=(340, 10))
		self.result = wx.TextCtrl(self, pos=(330, 30), size=(340, 175), style=wx.TE_MULTILINE | 										wx.TE_READONLY)

	def EvtWord(self, event):
		"""
		"""
		self.reword = event.GetString()

	def EvtComboBox(self, event):
		"""
		"""
		self.keynums = int(self.numlist[event.GetInt()])

	def OnclickButton1(self, event):
		"""
		"""
		self.result.Clear()
		try:
			self.rekey = self.model.relative_words(self.reword)
		except:
			self.result.AppendText('word %s is not in vocabulary\n' % (self.reword))

		for i in range(self.keynums):
			try:
				self.result.AppendText('relative%d: %s\n' %(i+1, 
								self.rekey[i][0]))		
			except:
				self.result.AppendText('relative%d: %s\n' %(i+1, ""))

	def OnclickButton2(self, event):
		"""
		"""
		with open('relatives', 'w') as f:
			for key in self.rekey:
				f.write("key: %s  value: %f\n" %(key[0], key[1]))


class AspectPanel(wx.Panel):
	"""
	"""

	def __init__(self, parent, model):
		"""
		"""
		wx.Panel.__init__(self, parent)
		self.model = model
		self.rekey = []
		self.resent = ""

		# input sentence
		self.lbgets = wx.StaticText(self, label="input a sentence here:", pos=(20, 10))
		self.sentence = wx.TextCtrl(self, pos=(20, 40), size=(280, 150), style=wx.TE_MULTILINE)
		self.Bind(wx.EVT_TEXT, self.EvtSentence, self.sentence)

		# comboBox
		self.maxnumlist = ['-', '2', '3', '5', '10']
		self.lblselnum = wx.StaticText(self, label="Select max_asps num:", pos=(30, 205))
		self.boxselnum = wx.ComboBox(self, pos=(190, 200), size=(95, -1), choices=self.maxnumlist, style=wx.CB_DROPDOWN)
		self.boxselnum.SetSelection(0)
		self.keynums = -1
		self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.boxselnum)

		# button1
		self.button1 = wx.Button(self, label="Execute", pos=(330, 215))
		self.Bind(wx.EVT_BUTTON, self.OnclickButton1, self.button1)

		# button2
		self.button2 = wx.Button(self, label="Save", pos=(430, 215))
		self.Bind(wx.EVT_BUTTON, self.OnclickButton2, self.button2)

		# result
		self.lbresult = wx.StaticText(self, label="aspect words :", pos=(340, 10))
		self.result = wx.TextCtrl(self, pos=(330, 30), size=(340, 175), style=wx.TE_MULTILINE | wx.TE_READONLY)

	def EvtSentence(self, event):
		"""
		"""
		self.resent = event.GetString()

	def EvtComboBox(self, event):
		"""
		"""
		if event.GetString() == '-':
			self.aspnums = -1
		else:
			self.aspnums = int(self.maxnumlist[event.GetInt()])

	def OnclickButton1(self, event):
		"""
		"""
		self.result.Clear()
		self.rekey = self.model.aspect(self.resent)

		if self.keynums == -1:
			max_num = len(self.rekey)
		else:
			max_num = self.keynums

		if max_num == 0:
			self.result.AppendText("This sentence cant not find any aspect word")

		for i in range(max_num):
			try:
				self.result.AppendText('aspword%d: %s\n' % (i + 1,
															self.rekey[i]))
			except:
				self.result.AppendText('aspword%d: %s\n' % (i + 1, ""))

	def OnclickButton2(self, event):
		"""
		"""
		with open('asps', 'w') as f:
			for key in self.rekey:
				f.write("asp: %s\n" % (key))

if __name__ == '__main__':
	model = MyModel('model/word2vec_wx', 'model/words.txt')
	app = wx.App()	
	frame = wx.Frame(None, title='Emotion analysis', size=(700,320), style=wx.CAPTION | 											wx.CLOSE_BOX)
	nb = wx.Notebook(frame)

	nb.AddPage(KeyWordsPanel(nb, model), "get keywords", True)
	nb.AddPage(RelativeWordsPanel(nb, model), "get relative words")
	nb.AddPage(AspectPanel(nb, model), "get aspects")
	frame.Show()
	nb.Refresh()
	app.MainLoop()

