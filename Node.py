# TODO：你返回一个list代表一个module，这个list是[Node1, Node2, ...], 由于Node的数据格式，list里面每个Node就可以对应ckt中的每一行
# ***************************Node Class***************************
# name: 门电路的名称，依照gtype = {'IPI'，'BRCH', 'xor','or', 'nor','inv','nand','and','xnor','aoi','oai','BUF'}
# 								IPI 是primary input，BRCH是branch，aoi是inv((x1 and x2)or x3), oai是inv((x1 or x2)and x3)
# type：ckt第一列
# id：ckt第二列，编码Mi_j
# gtype: ckt第三列，采用编码，gtype = {'IPI':0,'BRCH':1, 'xor':2,'or':3, 'nor':4,'inv':5,'nand':6,'and':7,'xnor':8,'aoi':9,'oai':10,'BUF':11}
# outline：ckt第四列
# inline：ckt第五列
# inputid：ckt第六列，这里要对应id的编码
# ****************************************************************
class Node():
	def __init__(self, name, type1, id1, gtype, outline, inline, inputid):
		self.name = name
		self.type = type1
		self.id = id1
		self.gtype = gtype
		self.outline = outline
		self.inline = inline
		self.inputid = inputid


# 这两行用于打印，直接print(Node1)或者print([Node1,Node2,...])均可以打印Node或者Node list的信息
	def __str__(self):
		return str(self.name)+'\t'+str(self.type)+'\t'+str(self.id)+'\t'+str(self.gtype)+'\t'+str(self.outline)+'\t'+str(self.inline)+'\t'+str(self.inputid)
	def __repr__(self):
		return str(self.name)+'\t'+str(self.type)+'\t'+str(self.id)+'\t'+str(self.gtype)+'\t'+str(self.outline)+'\t'+str(self.inline)+'\t'+str(self.inputid)
