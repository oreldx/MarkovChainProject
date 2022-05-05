import scrapetube
import io


def scrapTitleChannel(idChannel, filePath):
    videos = scrapetube.get_channel(idChannel)
    with io.open(filePath, 'a', encoding='utf-8') as file:
        for video in videos:
            title = video['title']['runs'][0]['text']
            file.write(title + '\n')


def scrap():
    channelsID = [
        'UCkcvvd77UoEXC-ahAkP4k8g',
        'UCoNvmftvPAAlozI-DTUrAng',
        'UCsM_9eGMTnp9AJVxroLlWkg'
    ]
    for channelID in channelsID:
        scrapTitleChannel(channelID, 'data/titlesRaw.txt')


if __name__ == '__main__':
    # scrapTitleChannel("UCkcvvd77UoEXC-ahAkP4k8g", 'test.txt')
    scrap()
