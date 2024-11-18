export default function createReportObject(employeesList) {
  const allEmployees = {};

  for (const [departmentName, employees] of Object.entries(employeesList)) {
    allEmployees[departmentName] = [...employees];
  }

  const getNumberOfDepartments = () => Object.keys(allEmployees).length;

  return {
    allEmployees,
    getNumberOfDepartments,
  };
}
