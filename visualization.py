from data_request import get_data_from_api
import matplotlib.pyplot as plt


def make_diagram(data: dict):
    # obtaining keys and values
    days = list(data.keys())
    values = list(data.values())

    # maiking diagram
    fig, ax = plt.subplots()
    fig.set_size_inches(5, 5)
    ax.axvline(x=5, color="gray", linestyle="--")
    colors = ["green" if v < 4 else "orange" if v < 5 else "red" for v in values]
    ax.barh(days, values, color=colors, edgecolor="black")
    for i, days in enumerate(days):
        ax.text(0.2, i, days, va='center', color='black', fontweight='bold')
        
    ax.set_yticklabels([])
    ax.invert_yaxis()
    
    # adding labels and title
    ax.set_xlabel("K-index")
    ax.set_title("Magnetic activity forecast")
         

if __name__ == "__main__":
    make_diagram(get_data_from_api())
    plt.show()
