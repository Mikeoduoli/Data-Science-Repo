-- select continent, MAX(CAST(total_deaths as int)) as TotalDeathCount
-- FROM public.covid_table
-- where continent is not null
-- GROUP BY continent
-- ORDER BY TotalDeathCount desc

-- Showing the continent with highest death count

select continent, MAX(CAST(total_deaths as int)) as TotalDeathCount
FROM public.covid_table
where continent is not null
GROUP BY continent
ORDER BY TotalDeathCount desc

-- Global numbers

Select location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 AS DeathPercentage
FROM public.covid_table
-- WHERE location like '%state%'
WHERE continent is not null
ORDER BY 1, 2

Select SUM(new_cases) AS total_cases, SUM(cast(new_deaths as int)) AS total_deaths, SUM(cast(new_deaths as int))/
SUM(new_cases)*100 as DeathPercentage -- (total_deaths/total_cases)*100 AS DeathPercentage
FROM public.covid_table
-- WHERE location like '%state%'
WHERE continent is not null
-- group by date
ORDER BY 1, 2


















