import glob, os, processing
path_to_shp = "C:/Users/ivan/Desktop/teste/" #pasta onde estão os shapefiles que vão ser mergeados
os.chdir(path_to_shp)
filelist = []
for fname in glob.glob("*.shp"):
    uri = path_to_shp + fname
    filelist.append(uri)

fileliststring = ';'.join(filelist)
processing.run(
    "qgis:mergevectorlayers",
    {
        "LAYERS": filelist,
        "OUTPUT": "C:/Users/ivan/Desktop/out/merged.shp", #diretório de saída do resultado do merge 
    },
)