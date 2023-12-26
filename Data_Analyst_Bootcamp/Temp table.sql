SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
	SUM(CAST(int, vac.new_vaccinations)) OVER (PARTITION BY dea.location, 
	dea.date) AS RollingPeopleVaccinated
FROM public.covid_table dea
JOIN public.covid_vaccinations vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not null
ORDER BY 2,3


-- USe CTE

WITH PopvsVac (continent, location, date, population, new_vaccinations, RollingPeopleVaccinated)
as
(
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
	SUM(CONVERT(int, vac.new_vaccinations)) OVER (PARTITION BY dea.location, 
	dea.date) AS RollingPeopleVaccinated
FROM public.covid_table dea
JOIN public.covid_vaccinations vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not null
-- ORDER BY 2,3
)

SELECT *, (RollingPeopleVaccinated/Population)*100
FROM PopvsVac


-- TEMP TABLE

DROP TABLE IF EXISTS #PercentPopulationVaccinated
CREATE TABLE #PercentPopulationVaccinated
(
	Continent nvarchar(255),
	Location nvarchar(255),
	Date datetime,
	Population numeric,
	New_vaccinations numeric,
	RollingPeopleVaccinated numeric
)

INSERT INTO
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
	SUM(CONVERT(int, vac.new_vaccinations)) OVER (PARTITION BY dea.location, 
	dea.date) AS RollingPeopleVaccinated
FROM public.covid_table dea
JOIN public.covid_vaccinations vac
	ON dea.location = vac.location
	AND dea.date = vac.date
-- WHERE dea.continent is not null
-- ORDER BY 2,3

SELECT *, (RollingPeopleVaccinated/Population)*100
FROM #PercentPopulationVaccinated


-- Creating View to store data for later visualizations

CREATE VIEW PercentPopulationVaccinated AS

SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
	SUM(CONVERT(int, vac.new_vaccinations)) OVER (PARTITION BY dea.location, 
	dea.date) AS RollingPeopleVaccinated
FROM public.covid_table dea
JOIN public.covid_vaccinations vac
	ON dea.location = vac.location
	AND dea.date = vac.date
WHERE dea.continent is not null
-- ORDER BY 2,3


































