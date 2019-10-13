import pandas

if __name__ == '__main__':
    print('Load data...')
    raw_data = (
        pandas.read_csv(
            '../data-raw/cargo_all_proj_commits.csv.gz',
            usecols=['full_name', 'author_name', 'date', 'author_github_username'],
            parse_dates=['date'],
        )
        .rename(columns={
            'full_name': 'project',
            'author_github_username': 'author',
        })
    )

    print('Projects:', len(raw_data.drop_duplicates('project')))
    print('Authors:', len(raw_data.drop_duplicates('author')))
    print('Commits:', len(raw_data))
    # print('Oldest:', raw_data['date'].min())
    # print('Latest:', raw_data['date'].max())

    print('Convert data...')
    df = (
        raw_data
        .assign(date=lambda d: d['date'].dt.date)
        .assign(commits=1)
        .groupby(['project', 'author', 'date'], as_index=False, sort=False)
        .agg({
            'author_name': 'first',
            'commits': 'count',
        })
        .drop_duplicates(['project', 'author', 'date'])
        .groupby(['author', 'project'], as_index=False, sort=False)
        .apply(lambda group:
            group
            .sort_values('date')
            .assign(duration=lambda d: (d['date'] - d['date'].shift(1)))
            .assign(truth=lambda d: (d['date'].shift(-1) - d['date']))
        )
        .reset_index()
        [['author', 'author_name', 'project', 'date', 'commits', 'duration', 'truth']]
    )
    
    print('Save data...')
    df.to_csv('./cargo.csv.gz', index=False, compression='gzip')