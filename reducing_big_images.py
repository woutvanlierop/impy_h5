import os
from impy.ObjectDetectionDataset import ObjectDetectionDataset

def main():
	# Define the path to images and annotations
	images_path:str = os.path.join(os.getcwd(), "insects_dataset", "images")
	annotations_path:str = os.path.join(os.getcwd(), "insects_dataset", "annotations", "xmls")
	# Define the name of the dataset
	dbName:str = "InsectsDataset"
	# Create an object of ObjectDetectionDataset
	obda:any = ObjectDetectionDataset(imagesDirectory=images_path, annotationsDirectory=annotations_path, databaseName=dbName)
	# Reduce the dataset to smaller Rois of smaller ROIs of shape 1032x1032.
	offset:list=[1032, 1032]
	images_output_path:str = os.path.join(os.getcwd(), "insects_dataset", "images_reduced")
	annotations_output_path:str = os.path.join(os.getcwd(), "insects_dataset", "annotations_reduced", "xmls")
	obda.reduceDatasetByRois(offset = offset, outputImageDirectory = images_output_path, outputAnnotationDirectory = annotations_output_path)

if __name__ == "__main__":
	main()
