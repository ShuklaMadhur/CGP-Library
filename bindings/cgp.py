# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cgp', [dirname(__file__)])
        except ImportError:
            import _cgp
            return _cgp
        if fp is not None:
            try:
                _mod = imp.load_module('_cgp', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _cgp = swig_import_helper()
    del swig_import_helper
else:
    import _cgp
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def initialiseParameters(*args):
  return _cgp.initialiseParameters(*args)
initialiseParameters = _cgp.initialiseParameters

def freeParameters(*args):
  return _cgp.freeParameters(*args)
freeParameters = _cgp.freeParameters

def printParameters(*args):
  return _cgp.printParameters(*args)
printParameters = _cgp.printParameters

def addNodeFunction(*args):
  return _cgp.addNodeFunction(*args)
addNodeFunction = _cgp.addNodeFunction

def addCustomNodeFunction(*args):
  return _cgp.addCustomNodeFunction(*args)
addCustomNodeFunction = _cgp.addCustomNodeFunction

def clearFunctionSet(*args):
  return _cgp.clearFunctionSet(*args)
clearFunctionSet = _cgp.clearFunctionSet

def setNumInputs(*args):
  return _cgp.setNumInputs(*args)
setNumInputs = _cgp.setNumInputs

def setNumNodes(*args):
  return _cgp.setNumNodes(*args)
setNumNodes = _cgp.setNumNodes

def setNumOutputs(*args):
  return _cgp.setNumOutputs(*args)
setNumOutputs = _cgp.setNumOutputs

def setArity(*args):
  return _cgp.setArity(*args)
setArity = _cgp.setArity

def setMu(*args):
  return _cgp.setMu(*args)
setMu = _cgp.setMu

def setLambda(*args):
  return _cgp.setLambda(*args)
setLambda = _cgp.setLambda

def setEvolutionaryStrategy(*args):
  return _cgp.setEvolutionaryStrategy(*args)
setEvolutionaryStrategy = _cgp.setEvolutionaryStrategy

def setMutationRate(*args):
  return _cgp.setMutationRate(*args)
setMutationRate = _cgp.setMutationRate

def setRecurrentConnectionProbability(*args):
  return _cgp.setRecurrentConnectionProbability(*args)
setRecurrentConnectionProbability = _cgp.setRecurrentConnectionProbability

def setConnectionWeightRange(*args):
  return _cgp.setConnectionWeightRange(*args)
setConnectionWeightRange = _cgp.setConnectionWeightRange

def setCustomFitnessFunction(*args):
  return _cgp.setCustomFitnessFunction(*args)
setCustomFitnessFunction = _cgp.setCustomFitnessFunction

def setCustomSelectionScheme(*args):
  return _cgp.setCustomSelectionScheme(*args)
setCustomSelectionScheme = _cgp.setCustomSelectionScheme

def setCustomReproductionScheme(*args):
  return _cgp.setCustomReproductionScheme(*args)
setCustomReproductionScheme = _cgp.setCustomReproductionScheme

def setTargetFitness(*args):
  return _cgp.setTargetFitness(*args)
setTargetFitness = _cgp.setTargetFitness

def setMutationType(*args):
  return _cgp.setMutationType(*args)
setMutationType = _cgp.setMutationType

def setUpdateFrequency(*args):
  return _cgp.setUpdateFrequency(*args)
setUpdateFrequency = _cgp.setUpdateFrequency

def initialiseChromosome(*args):
  return _cgp.initialiseChromosome(*args)
initialiseChromosome = _cgp.initialiseChromosome

def initialiseChromosomeFromFile(*args):
  return _cgp.initialiseChromosomeFromFile(*args)
initialiseChromosomeFromFile = _cgp.initialiseChromosomeFromFile

def initialiseChromosomeFromChromosome(*args):
  return _cgp.initialiseChromosomeFromChromosome(*args)
initialiseChromosomeFromChromosome = _cgp.initialiseChromosomeFromChromosome

def freeChromosome(*args):
  return _cgp.freeChromosome(*args)
freeChromosome = _cgp.freeChromosome

def printChromosome(*args):
  return _cgp.printChromosome(*args)
printChromosome = _cgp.printChromosome

def executeChromosome(*args):
  return _cgp.executeChromosome(*args)
executeChromosome = _cgp.executeChromosome

def getChromosomeOutput(*args):
  return _cgp.getChromosomeOutput(*args)
getChromosomeOutput = _cgp.getChromosomeOutput

def saveChromosome(*args):
  return _cgp.saveChromosome(*args)
saveChromosome = _cgp.saveChromosome

def saveChromosomeDot(*args):
  return _cgp.saveChromosomeDot(*args)
saveChromosomeDot = _cgp.saveChromosomeDot

def saveChromosomeLatex(*args):
  return _cgp.saveChromosomeLatex(*args)
saveChromosomeLatex = _cgp.saveChromosomeLatex

def mutateChromosome(*args):
  return _cgp.mutateChromosome(*args)
mutateChromosome = _cgp.mutateChromosome

def removeInactiveNodes(*args):
  return _cgp.removeInactiveNodes(*args)
removeInactiveNodes = _cgp.removeInactiveNodes

def setChromosomeFitness(*args):
  return _cgp.setChromosomeFitness(*args)
setChromosomeFitness = _cgp.setChromosomeFitness

def resetChromosome(*args):
  return _cgp.resetChromosome(*args)
resetChromosome = _cgp.resetChromosome

def copyChromosome(*args):
  return _cgp.copyChromosome(*args)
copyChromosome = _cgp.copyChromosome

def getNumChromosomeInputs(*args):
  return _cgp.getNumChromosomeInputs(*args)
getNumChromosomeInputs = _cgp.getNumChromosomeInputs

def getNumChromosomeNodes(*args):
  return _cgp.getNumChromosomeNodes(*args)
getNumChromosomeNodes = _cgp.getNumChromosomeNodes

def getNumChromosomeActiveNodes(*args):
  return _cgp.getNumChromosomeActiveNodes(*args)
getNumChromosomeActiveNodes = _cgp.getNumChromosomeActiveNodes

def getNumChromosomeOutputs(*args):
  return _cgp.getNumChromosomeOutputs(*args)
getNumChromosomeOutputs = _cgp.getNumChromosomeOutputs

def getChromosomeNodeArity(*args):
  return _cgp.getChromosomeNodeArity(*args)
getChromosomeNodeArity = _cgp.getChromosomeNodeArity

def getChromosomeFitness(*args):
  return _cgp.getChromosomeFitness(*args)
getChromosomeFitness = _cgp.getChromosomeFitness

def getChromosomeGenerations(*args):
  return _cgp.getChromosomeGenerations(*args)
getChromosomeGenerations = _cgp.getChromosomeGenerations

def initialiseDataSetFromArrays(*args):
  return _cgp.initialiseDataSetFromArrays(*args)
initialiseDataSetFromArrays = _cgp.initialiseDataSetFromArrays

def initialiseDataSetFromFile(*args):
  return _cgp.initialiseDataSetFromFile(*args)
initialiseDataSetFromFile = _cgp.initialiseDataSetFromFile

def freeDataSet(*args):
  return _cgp.freeDataSet(*args)
freeDataSet = _cgp.freeDataSet

def printDataSet(*args):
  return _cgp.printDataSet(*args)
printDataSet = _cgp.printDataSet

def saveDataSet(*args):
  return _cgp.saveDataSet(*args)
saveDataSet = _cgp.saveDataSet

def getNumDataSetInputs(*args):
  return _cgp.getNumDataSetInputs(*args)
getNumDataSetInputs = _cgp.getNumDataSetInputs

def getNumDataSetOutputs(*args):
  return _cgp.getNumDataSetOutputs(*args)
getNumDataSetOutputs = _cgp.getNumDataSetOutputs

def getNumDataSetSamples(*args):
  return _cgp.getNumDataSetSamples(*args)
getNumDataSetSamples = _cgp.getNumDataSetSamples

def getDataSetSampleInputs(*args):
  return _cgp.getDataSetSampleInputs(*args)
getDataSetSampleInputs = _cgp.getDataSetSampleInputs

def getDataSetSampleInput(*args):
  return _cgp.getDataSetSampleInput(*args)
getDataSetSampleInput = _cgp.getDataSetSampleInput

def getDataSetSampleOutputs(*args):
  return _cgp.getDataSetSampleOutputs(*args)
getDataSetSampleOutputs = _cgp.getDataSetSampleOutputs

def getDataSetSampleOutput(*args):
  return _cgp.getDataSetSampleOutput(*args)
getDataSetSampleOutput = _cgp.getDataSetSampleOutput

def freeResults(*args):
  return _cgp.freeResults(*args)
freeResults = _cgp.freeResults

def saveResults(*args):
  return _cgp.saveResults(*args)
saveResults = _cgp.saveResults

def getChromosome(*args):
  return _cgp.getChromosome(*args)
getChromosome = _cgp.getChromosome

def getNumChromosomes(*args):
  return _cgp.getNumChromosomes(*args)
getNumChromosomes = _cgp.getNumChromosomes

def getAverageFitness(*args):
  return _cgp.getAverageFitness(*args)
getAverageFitness = _cgp.getAverageFitness

def getMedianFitness(*args):
  return _cgp.getMedianFitness(*args)
getMedianFitness = _cgp.getMedianFitness

def getAverageActiveNodes(*args):
  return _cgp.getAverageActiveNodes(*args)
getAverageActiveNodes = _cgp.getAverageActiveNodes

def getMedianActiveNodes(*args):
  return _cgp.getMedianActiveNodes(*args)
getMedianActiveNodes = _cgp.getMedianActiveNodes

def getAverageGenerations(*args):
  return _cgp.getAverageGenerations(*args)
getAverageGenerations = _cgp.getAverageGenerations

def getMedianGenerations(*args):
  return _cgp.getMedianGenerations(*args)
getMedianGenerations = _cgp.getMedianGenerations

def runCGP(*args):
  return _cgp.runCGP(*args)
runCGP = _cgp.runCGP

def repeatCGP(*args):
  return _cgp.repeatCGP(*args)
repeatCGP = _cgp.repeatCGP

def setRandomNumberSeed(*args):
  return _cgp.setRandomNumberSeed(*args)
setRandomNumberSeed = _cgp.setRandomNumberSeed
# This file is compatible with both classic and new-style classes.


