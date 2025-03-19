import viennals2d as vls
import viennaps2d as vps

vps.Logger.setLogLevel(vps.LogLevel.INFO)

domain = vps.Domain()
vps.MakePlane(domain, .2, 100., 0., 0., False, vps.Material.Si).apply()
domain.saveVolumeMesh("step_1")

vps.MakePlane(domain, 10., vps.Material.Si3N4).apply()
domain.saveVolumeMesh("step_2")

box = vls.lsDomain(domain.getLevelSets()[-1])
vls.lsMakeGeometry(box, vls.lsBox([-20., 0., 0.], [20., 11., 10.])).apply()
domain.applyBooleanOperation(box, vls.lsBooleanOperationEnum.RELATIVE_COMPLEMENT)
domain.saveVolumeMesh("step_3")

dirEtch = vps.DirectionalEtching([0., -1., 0.], 1., -0.1, vps.Material.Si3N4)
vps.Process(domain, dirEtch, 50.).apply()
domain.saveVolumeMesh("step_4")

domain.duplicateTopLevelSet(vps.Material.SiO2)

iso = vps.IsotropicProcess(1., vps.Material.Si3N4)
vps.Process(domain, iso, 2.).apply()
domain.saveVolumeMesh("step_5")

domain.duplicateTopLevelSet(vps.Material.Al2O3)

iso = vps.IsotropicProcess(1.)
vps.Process(domain, iso, 10.).apply()
domain.saveVolumeMesh("step_6")

levelsets = domain.getLevelSets()
for i, ls in enumerate(levelsets):
    mesh = vls.lsMesh()
    vls.lsToSurfaceMesh(ls, mesh).apply()
    vls.lsVTKWriter(mesh, "cvd_" + str(i) + ".vtp").apply()
