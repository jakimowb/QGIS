# The following has been generated automatically from src/core/network/qgsnetworkcontentfetcherregistry.h
QgsFetchedContent.NotStarted = QgsFetchedContent.ContentStatus.NotStarted
QgsFetchedContent.Downloading = QgsFetchedContent.ContentStatus.Downloading
QgsFetchedContent.Finished = QgsFetchedContent.ContentStatus.Finished
QgsFetchedContent.Failed = QgsFetchedContent.ContentStatus.Failed
try:
    QgsFetchedContent.__attribute_docs__ = {'fetched': 'Emitted when the file is fetched and accessible\n', 'errorOccurred': 'Emitted when an error with ``code`` error occurred while processing the\nrequest ``errorMsg`` is a textual description of the error\n\n.. versionadded:: 3.22\n'}
    QgsFetchedContent.__signal_arguments__ = {'errorOccurred': ['code: QNetworkReply.NetworkError', 'errorMsg: str']}
    QgsFetchedContent.__group__ = ['network']
except (NameError, AttributeError):
    pass
try:
    QgsNetworkContentFetcherRegistry.__group__ = ['network']
except (NameError, AttributeError):
    pass
