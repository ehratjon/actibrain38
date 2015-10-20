from nilearn import datasets
import matplotlib.pyplot as plt
from nilearn import plotting

def plot_activation_by_ID(identifier):
	localizer_dataset = datasets.fetch_localizer_contrasts(
		[identifier],
		n_subjects=2,
		get_tmaps=True)
	localizer_tmap_filenme = localizer_dataset.tmaps[1]

	plotting.plot_glass_brain(localizer_tmap_filename,
		threshold=3)
def plot_activation_by_data(localizer_ddata):
	plotting.plot_glass_brain(localizer_data, threshold=3)
