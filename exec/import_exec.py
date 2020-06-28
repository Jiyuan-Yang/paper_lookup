from utils.output import notify_print


def import_exec(args, parser_import):
    no_bib = args.no_bib  # set --no-bib flag to eliminate warnings
    folder = args.folder
    single = args.single
    if not (folder or single):
        notify_print('error', 'Please set either a folder or a single file to import')
        exit(0)
    if no_bib:
        notify_print('warning', '--no-bib flag has been set, there will be no more '
                                'warnings about the absent bib files')
