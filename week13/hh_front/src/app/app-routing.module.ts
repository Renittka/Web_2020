import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CompanyDetailComponent} from './company-detail/company-detail.component';
import { CompaniesListComponent } from './companies-list/companies-list.component';

const routes: Routes = [
  { path: '', component: CompaniesListComponent },
  { path: 'company/:id', component: CompanyDetailComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
